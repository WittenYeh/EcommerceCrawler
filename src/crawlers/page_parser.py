# data_parser.py
import json
import re
import requests
from bs4 import BeautifulSoup

class PageParser:
    """
    A reusable parser for extracting product information from 1688.com HTML content.
    Instantiate this class once and use the `parse` method for multiple HTML documents.
    """

    def _extract_init_data(self, soup: BeautifulSoup) -> dict:
        """Extracts the 'window.__INIT_DATA' JSON object from the HTML."""
        script_tag = soup.find("script", string=re.compile("window.__INIT_DATA"))
        if not script_tag:
            print("Could not find __INIT_DATA script tag.")
            return {}
        
        json_str_match = re.search(r"window\.__INIT_DATA\s*=\s*({.*});", script_tag.string)
        if not json_str_match:
            print("Could not extract JSON data from script tag.")
            return {}
        
        try:
            return json.loads(json_str_match.group(1))
        except json.JSONDecodeError:
            print("Failed to parse JSON data.")
            return {}

    def _find_module_data(self, all_data_modules: dict, component_type: str) -> dict:
        """Finds module data by componentType, as module IDs can be dynamic."""
        for key in all_data_modules:
            module = all_data_modules[key]
            if isinstance(module, dict) and module.get("componentType") == component_type:
                return module.get("data", {})
        return {}

    def _get_description(self, data: dict) -> str:
        """Fetches and cleans the detailed product description."""
        description_data = self._find_module_data(data.get("data", {}), "@ali/tdmod-od-pc-offer-description")
        desc_url = description_data.get('detailUrl')
        if not desc_url:
            return "Description not found."
            
        try:
            desc_response = requests.get("https:" + desc_url, timeout=10).text
            desc_html_raw = re.search(r'{"content":"(.*)"}', desc_response)
            if desc_html_raw:
                # Clean up escaped characters
                return desc_html_raw.group(1).replace('\\"', '"').replace('\\/', '/')
        except requests.RequestException as e:
            print(f"Could not fetch description: {e}")
        return "Could not fetch description."

    def parse(self, html_content: str) -> list:
        """
        Main parsing method to extract all product variants from a given HTML content.

        Args:
            html_content (str): The HTML content of the product page.

        Returns:
            list: A list of dictionaries, where each dictionary is a product variant.
        """
        if not html_content:
            print("HTML content is empty. Skipping parse.")
            return []

        soup = BeautifulSoup(html_content, 'lxml')
        data = self._extract_init_data(soup)

        if not data:
            print("Could not extract initial data. Skipping parse.")
            return []

        # --- Extract common data ---
        all_data_modules = data.get("data", {})
        global_data = data.get("globalData", {})
        
        title_data = self._find_module_data(all_data_modules, "@ali/tdmod-od-pc-offer-title") or \
                     self._find_module_data(all_data_modules, "@ali/tdmod-od-gyp-pc-offer-title")
        main_pic_data = self._find_module_data(all_data_modules, "@ali/tdmod-pc-od-main-pic") or \
                        self._find_module_data(all_data_modules, "@ali/tdmod-od-gyp-pc-main-pic")
        attribute_data = self._find_module_data(all_data_modules, "@ali/tdmod-od-pc-attribute-new")
        cross_border_data = self._find_module_data(all_data_modules, "@ali/tdmod-od-pc-offer-cross")

        title = title_data.get("title") or global_data.get("tempModel", {}).get("offerTitle", "Title Not Found")
        photo_list = [img.get("fullPathImageURI") for img in main_pic_data.get("mainImage", []) if img.get("fullPathImageURI")]
        photos_str = ", ".join(photo_list)
        
        attributes = {attr['name']: attr['value'] for attr in attribute_data if 'name' in attr and 'value' in attr}
        brand = attributes.get("品牌", "N/A")
        composition = attributes.get("成分及含量") or attributes.get("主要用途")
        upc = attributes.get("商品条形码", "Not Available")
        description = self._get_description(data)
        
        base_product = {
            "Title": title, "Photos": photos_str, "Universal product code": upc,
            "Description": description, "Brand": brand, "Composition": composition,
            "(Colombia) Listing type": "Classic", "Warranty type": "No warranty",
            "Gender": "Gender neutral", "Package weight unit": "g",
            "Package length, width and height unit": "cm",
        }
        
        # --- SKU-specific data ---
        all_variants = []
        sku_selection_data = self._find_module_data(all_data_modules, "@ali/tdmod-gyp-pc-sku-selection") or \
                             self._find_module_data(all_data_modules, "@ali/tdmod-pc-od-dsc-order")
        
        # Structure for Industrial Product Pages (gyp-pc)
        if sku_selection_data and 'modelSelectionInfo' in sku_selection_data:
            price_data = self._find_module_data(all_data_modules, "@ali/tdmod-od-pc-offer-price")
            all_sku_details = price_data.get('finalPriceModel', {}).get('tradeWithoutPromotion', {}).get('skuMap', [])
            
            for sku_item in sku_selection_data.get('modelSelectionInfo', {}).get('data', []):
                sku_props = {prop['name']: prop['value'] for prop in sku_item.get('props', [])}
                sku_id = sku_item.get('skuId')
                details = next((s for s in all_sku_details if s.get("skuId") == sku_id), {})
                
                pkg_info = {}
                if cross_border_data.get('pieceWeightScale', {}).get('pieceWeightScaleInfo'):
                    pkg_item = next((p for p in cross_border_data['pieceWeightScale']['pieceWeightScaleInfo'] if p.get("skuId") == sku_id), None)
                    if pkg_item:
                         pkg_info = {
                            'weight': int(float(pkg_item.get('weight', 100))), 'length': int(float(pkg_item.get('length', 10))),
                            'width': int(float(pkg_item.get('width', 10))), 'height': int(float(pkg_item.get('height', 10))),
                        }

                variant = base_product.copy()
                variant.update({
                    "SKU": sku_item.get('name', 'N/A'),
                    "Color": sku_props.get('颜色', 'N/A'),
                    "Stock": int(details.get("canBookCount", 0)),
                    "(Colombia) Price in US": float(details.get("price", 0.0)),
                    "Package gross weight": pkg_info.get('weight', 100),
                    "Package length": pkg_info.get('length', 10),
                    "Package width": pkg_info.get('width', 10),
                    "Package height": pkg_info.get('height', 10),
                })
                all_variants.append(variant)

        return all_variants
