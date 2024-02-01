def write_file(file_name, file_content):
    
    file_name_with_extension = file_name + '.txt'

   
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)

def append_to_file(file_name, file_content):
    
   
    file_name_with_extension = file_name + '.txt'

    
    with open(file_name_with_extension, 'a') as file:
        file.write(file_content)

def read_file(file_name):
    """
    Read and return the content of the .txt file specified by file_name.
    If the file doesn't exist, return an empty string.
    """
   
    file_name_with_extension = file_name + '.txt'

    try:
        
        with open(file_name_with_extension, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
       
        return ""


file_name = "example_file"


write_file(file_name, "This is the content of the file.")


append_to_file(file_name, "\nThis is additional content appended to the file.")


content = read_file(file_name)
print("File content:")
print(content)

