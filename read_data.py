from config import path
# Function to read a text file and print its contents
def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your text file
file_path = path +'Documents//epic.txt'

# Call the function to read and print the file's contents
read_text_file(file_path)
