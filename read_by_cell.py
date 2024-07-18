import pandas as pd
from config import path

# Function to read a specific cell from an Excel file
def get_cell_value(file_path, sheet_name, row_index, column_header):
    try:
        # Read the specified sheet from the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Get the value of the specified cell
        cell_value = df.at[row_index, column_header]
        
        # Print the cell value
        print(f"Value at row {row_index}, column '{column_header}': {cell_value}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except KeyError:
        print(f"The column '{column_header}' does not exist in the sheet.")
    except IndexError:
        print(f"The row index {row_index} is out of bounds.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your Excel file and the sheet name
file_path = path+'//excel_sample_data.xlsx'
sheet_name = 'Sheet1'  # Replace with the name of the sheet you want to read
row_index = 0  # Replace with the row index of the cell you want to read
column_header = 'head1'  # Replace with the column header of the cell you want to read

# Call the function to get and print the cell value
get_cell_value(file_path, sheet_name, row_index, column_header)
