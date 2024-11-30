def modify_content(content):
   
    return content.upper()

def read_and_write_files():
    try:
        input_filename = input("Enter the name of the file to read from: ")
        with open(input_filename, 'r') as infile:
            content = infile.read()

        modified_content = modify_content(content)

        output_filename = input("Enter the name of the file to write to: ")
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content has been successfully read from {input_filename} and written to {output_filename}.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file cannot be read.")

read_and_write_files()
