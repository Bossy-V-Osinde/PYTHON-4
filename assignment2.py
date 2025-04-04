# Error Handling Lab
def handle_file_error():
    # Input filename is fixed as input.txt
    input_filename = "input.txt"

    try:
        # Step 1: Attempt to open and read the input file
        with open(input_filename, 'r') as file:
            content = file.read()
            print("File content successfully read:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
handle_file_error()
