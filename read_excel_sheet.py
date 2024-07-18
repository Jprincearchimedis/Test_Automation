import pandas as pd
from config import path

# Function to read a specific sheet from an Excel file
def read_excel_sheet(file_path, sheet_name):
    try:
        # Read the specified sheet from the Excel file
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # Print the contents of the sheet
        print(df)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except ValueError:
        print(f"The sheet '{sheet_name}' does not exist in the Excel file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your Excel file and the sheet name
file_path = path+'excel_sample_data.xlsx'
sheet_name = 'Sheet1'  # Replace with the name of the sheet you want to read

# Call the function to read and print the sheet's contents
read_excel_sheet(file_path, sheet_name)
