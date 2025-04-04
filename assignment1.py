# File Read & Write Challenge
def read_and_write_file():
    # Input filename is fixed as input.txt
    input_filename = "input.txt"

    # Step 1: Open and read the content of the input file
    with open(input_filename, 'r') as file:
        content = file.read()

    # Step 2: Modify the content (convert it to uppercase as an example)
    modified_content = content.upper()
    modified_content = modified_content.replace(" ", "_")  # Replace spaces with underscores
    word_count = len(content.split())  # Count the number of words

    # Step 3: Write the modified content to output.txt
    output_filename = "output.txt"
    with open(output_filename, 'w') as new_file:
        new_file.write(modified_content)
        new_file.write(f"\n\nWord Count: {word_count}")
    

    print(f"File '{output_filename}' has been created successfully with the modified content.")

# Call the function
read_and_write_file()
