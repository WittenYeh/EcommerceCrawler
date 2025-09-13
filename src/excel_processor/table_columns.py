class TableColumn:
    def __init__(
        self, 
        col_name: str, 
        col_index: int, 
        optional: bool = False, 
        auto_fill: bool = False, 
        data_type: type = str, 
        choices: list = None
    ):
        self.col_name = col_name
        self.col_index = col_index
        self.optional = optional
        self.auto_fill = auto_fill
        self.data_type = data_type
        self.choices = choices
        
columns = {
    # Required
    "Title": TableColumn(
        col_name="Title", 
        col_index=1, 
        optional=False, 
        auto_fill=False, 
        data_type=str
    ),
    # Auto filled and can be ignored
    "Number of characters": TableColumn(
        col_name="Number of characters", 
        col_index=2, 
        optional=False, 
        auto_fill=True, 
        data_type=int
    ),
    # Optional
    "SKU": TableColumn(
        col_name="SKU", 
        col_index=3, 
        optional=True,
        auto_fill=False,
        data_type=str
    ),
    # Required, type or select a value
    "Color": TableColumn(
        col_name="Color", 
        col_index=4, 
        optional=False, 
        auto_fill=False, 
        data_type=str
    ),
    # Optional
    "Varies in: Size": TableColumn(
        col_name="Varies in: Size", 
        col_index=5, 
        optional=True, 
        auto_fill=False, 
        data_type=str
    ),
    # Required, Access the Photo manager to obtain the URLs. Then, return to this spreadsheet and paste them in their corresponding cells.
    "Photos": TableColumn(
        col_name="Photos", 
        col_index=6, 
        optional=False, 
        auto_fill=False, 
        data_type=str
    ),
    # Required, It is usually an EAN, UPC or other GTIN.
    "Universal product code": TableColumn(
        col_name="Universal product code", 
        col_index=7, 
        optional=False, 
        auto_fill=False, 
        data_type=str
    ),
    # Required
    "Stock": TableColumn(
        col_name="Stock", 
        col_index=8, 
        optional=False, 
        auto_fill=False, 
        data_type=int
    ),
    # (Up to 2 decimal places) If you leave the price field empty, the product will not be listed in this country.
    "(Colombia) Price in US$": TableColumn(
        col_name="(Colombia) Price in US$", 
        col_index=9, 
        optional=False, 
        auto_fill=False, 
        data_type=float
    ),
    # Selected from ["Premium", "Classic"]
    "(Colombia) Listing type": TableColumn(
        col_name="(Colombia) Listing type", 
        col_index=10, 
        optional=False, 
        auto_fill=False, 
        data_type=str,
        choices=["Premium", "Classic"]
    ),
    # Auto filled and can be ignored
    "(Colombia) Selling Fee in US$": TableColumn(
        col_name="(Colombia) Selling Fee in US$", 
        col_index=11, 
        optional=False, 
        auto_fill=True, 
        data_type=float
    ),
    # (Up to 2 decimal places) If you leave the price field empty, the product will not be listed in this country.
    "(Brazil) Price in US$": TableColumn(
        col_name="(Brazil) Price in US$", 
        col_index=12, 
        optional=False, 
        auto_fill=False, 
        data_type=float
    ),
    # Selected from ["Premium", "Classic"]
    "(Brazil) Listing type": TableColumn(
        col_name="(Brazil) Listing type", 
        col_index=13, 
        optional=False, 
        auto_fill=False, 
        data_type=str,
        choices=["Premium", "Classic"]
    ),
    # Auto filled and can be ignored
    "(Brazil) Selling Fee in US$": TableColumn(
        col_name="(Brazil) Selling Fee in US$", 
        col_index=14, 
        optional=False, 
        auto_fill=True, 
        data_type=float
    ),
    # (Up to 2 decimal places) If you leave the price field empty, the product will not be listed in this country
    "(Chile) Price in US$": TableColumn(
        col_name="(Chile) Price in US$", 
        col_index=15, 
        optional=False, 
        auto_fill=False, 
        data_type=float
    ),
    # Selected from ["Premium", "Classic"]
    "(Chile) Listing type": TableColumn(
        col_name="(Chile) Listing type", 
        col_index=16, 
        optional=False, 
        auto_fill=False, 
        data_type=str,
        choices=["Premium", "Classic"]
    ),
    # Auto filled and can be ignored
    "(Chile) Selling Fee in US$": TableColumn(
        col_name="(Chile) Selling Fee in US$", 
        col_index=17, 
        optional=False, 
        auto_fill=True, 
        data_type=float
    ),
    # (Up to 2 decimal places) If you leave the price field empty, the product will not be listed in this country
    "(Mexico) Price in US$": TableColumn(
        col_name="(Mexico) Price in US$", 
        col_index=18, 
        optional=False, 
        auto_fill=False, 
        data_type=float
    ),
    # Selected from ["Premium", "Classic"]
    "(Mexico) Listing type": TableColumn(
        col_name="(Mexico) Listing type", 
        col_index=19, 
        optional=False, 
        auto_fill=False, 
        data_type=str,
        choices=["Premium", "Classic"]
    ),
    # Auto filled and can be ignored
    "(Mexico) Selling Fee in US$": TableColumn(
        col_name="(Mexico) Selling Fee in US$", 
        col_index=20, 
        optional=False, 
        auto_fill=True, 
        data_type=float
    ),
    # (Up to 2 decimal places) If you leave the price field empty, the product will not be listed in this country
    "(Mexico Fulfillment) Price in US$": TableColumn(
        col_name="(Mexico Fulfillment) Price in US$", 
        col_index=21, 
        optional=False, 
        auto_fill=False, 
        data_type=float
    ),
    # Selected from ["Premium", "Classic"]
    "(Mexico Fulfillment) Listing type": TableColumn(
        col_name="(Mexico Fulfillment) Listing type", 
        col_index=22, 
        optional=False, 
        auto_fill=False, 
        data_type=str,
        choices=["Premium", "Classic"]
    ),
    # Auto filled and can be ignored
    "(Mexico Fulfillment) Selling Fee in US$": TableColumn(
        col_name="(Mexico Fulfillment) Selling Fee in US$", 
        col_index=23, 
        optional=False, 
        auto_fill=True, 
        data_type=float
    ),
    # Optional
    "Description": TableColumn(
        col_name="Description", 
        col_index=24, 
        optional=True, 
        auto_fill=False, 
        data_type=str
    ),
    # Optional, Selected from ["Seller warranty", "Factory warranty", "No warranty"]
    "Warranty type": TableColumn(
        col_name="Warranty type", 
        col_index=25, 
        optional=True, 
        auto_fill=False, 
        data_type=str,
        choices=["Seller warranty", "Factory warranty", "No warranty"]
    ),
    # Optional, Integer only
    "Warranty time": TableColumn(
        col_name="Warranty time", 
        col_index=26, 
        optional=True, 
        auto_fill=False, 
        data_type=int
    ),
    # Optional, Selected from ["days", "months", "years"]
    "Warranty time unit": TableColumn(
        col_name="Warranty time unit", 
        col_index=27, 
        optional=True, 
        auto_fill=False, 
        data_type=str,
        choices=["days", "months", "years"]
    ),
    # Required
    "Brand": TableColumn(
        col_name="Brand", 
        col_index=28, 
        optional=False, 
        auto_fill=False, 
        data_type=str
    ),
    # Required, Selected from ["Woman", "Man", "Girls", "Babies", "Gender neutral", "Boys"]
    "Gender": TableColumn(
        col_name="Gender", 
        col_index=29, 
        optional=False, 
        auto_fill=False, 
        data_type=str,
        choices=["Woman", "Man", "Girls", "Babies", "Gender neutral", "Boys"]
    ),
    # Optional
    "Character": TableColumn(
        col_name="Character", 
        col_index=30, 
        optional=True, 
        auto_fill=False, 
        data_type=str
    ),
    # Optional, Numbers only
    "Costumes number": TableColumn(
        col_name="Costumes number", 
        col_index=31, 
        optional=True, 
        auto_fill=False, 
        data_type=int
    ),
    # Optional
    "Main material": TableColumn(
        col_name="Main material", 
        col_index=32, 
        optional=True, 
        auto_fill=False, 
        data_type=str
    ),
    # Optional
    "Composition": TableColumn(
        col_name="Composition", 
        col_index=33, 
        optional=True, 
        auto_fill=False, 
        data_type=str
    ),
    # Optional
    "Accessories included": TableColumn(
        col_name="Accessories included", 
        col_index=34, 
        optional=True, 
        auto_fill=False, 
        data_type=str
    ),
    # Required, Numbers only
    "Package gross weight": TableColumn(
        col_name="Package gross weight", 
        col_index=35, 
        optional=False, 
        auto_fill=False, 
        data_type=int
    ),
    # Required, Select from ["g", "kg", "lb", "mg", "oz"]
    "Package weight unit": TableColumn(
        col_name="Package weight unit", 
        col_index=36, 
        optional=False, 
        auto_fill=False, 
        data_type=str,
        choices=["g", "kg", "lb", "mg", "oz"]
    ),
    # Required, Numbers only
    "Package length": TableColumn(
        col_name="Package length", 
        col_index=37, 
        optional=False, 
        auto_fill=False, 
        data_type=int
    ),
    # Required, Numbers only
    "Package width": TableColumn(
        col_name="Package width", 
        col_index=38, 
        optional=False, 
        auto_fill=False, 
        data_type=int
    ),
    # Required, Numbers only
    "Package height": TableColumn(
        col_name="Package height", 
        col_index=39, 
        optional=False, 
        auto_fill=False, 
        data_type=int
    ),
    # Required, Select from ["cm", "ft", "m", "mm"]
    "Package length, width and height unit": TableColumn(
        col_name="Package length, width and height unit", 
        col_index=40, 
        optional=False, 
        auto_fill=False, 
        data_type=str,
        choices=["cm", "ft", "m", "mm"]
    )
}
