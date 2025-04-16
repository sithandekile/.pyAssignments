# Reading an existing file
try:
    source_filename = input("Enter the name of the file you want to read: ")
    with open(source_filename, "r") as source_file:
        existing_content = source_file.read()
        print(existing_content)

    # Creating and writing a new file
    new_filename = input("Enter the name of your new file: ")
    added_content = input("Write the content you want to add: ")
    with open(new_filename, 'w') as new_file:
        combined_content = existing_content + '\n' + added_content
        new_file.write(combined_content)
    print(f"File created successfully: {combined_content}")
except FileNotFoundError:
    print("File does not exist. ")
