from crawler_1688 import WebCrawler
from page_parser import PageParser

if __name__ == "__main__":
    offer_ids = ["871505026881", "885695622817"]
    scraper = WebCrawler()
    parser = PageParser()
    for offer_id in offer_ids:
        print(f"\n--- Processing Product ID: {offer_id} ---")
        
        html_content = scraper.fetch_html(offer_id)
        if not html_content:
            print(f"Skipping product {offer_id} due to fetch error.")
            continue
            
        try:
            product_variants = parser.parse(html_content)
            if not product_variants:
                print(f"No variants found or parsed for product {offer_id}.")
                continue
        except Exception as e:
            print(f"An error occurred during parsing for product {offer_id}: {e}")
            continue

        print(f"Found {len(product_variants)} variants")
        print(product_variants)