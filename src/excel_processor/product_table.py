import openpyxl
from enum import Enum, auto
from table_columns import TableColumn, columns

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

class ProductTable:
    
    def __init__(self, file_path: str):
        """ Initialize the ProductTable by loading the workbook and selecting the active sheet.
        
        Args:
            file_path (str): The path to the Excel file.
        """
        self.start_row = 7
        self.current_row = self.start_row
        self.workbook = openpyxl.load_workbook(file_path)
        self.sheet = self.workbook.active  # or specify a sheet name: self.workbook['Sheet1']
    
    def write_cell(self, row: int, column_name: str, value):
        """ Write a value to a specific cell in the product table.
        
        Args:
            row (int): The row number (1-indexed).
            column_name (str): The name of the column as defined in the `columns` dictionary.
            value: The value to write to the cell.
        """
        if column_name not in columns:
            raise ValueError(f"Column '{column_name}' is not defined in the product table.")

        col = columns[column_name].col_index
        cell = self.sheet.cell(row=row, column=col)
        cell.value = value
        
    def save(self, file_path: str):
        """ Save the workbook to the specified file path.
        
        Args:
            file_path (str): The path to save the workbook.
        """
        self.workbook.save(file_path)
    
    def acquire_new_row(self) -> int:
        """ Acquire the next available row for data entry.
        
        Returns:
            int: The next available row number (1-indexed).
        """
        current = self.current_row
        self.current_row += 1
        return current