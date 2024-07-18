import pandas as pd
from config import path

# Function to read an Excel file and print its contents
def read_excel_file(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Print the contents of the Excel file
        print(df)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your Excel file
file_path = path+'excel_sample_data.xlsx'

# Call the function to read and print the file's contents
read_excel_file(file_path)
