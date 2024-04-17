#!/usr/python3/bin

def append_after(filename="", search_string="", new_string=""):
    # Temporary file to store the modified content
    temp_filename = filename + ".tmp"
    
    with open(filename, 'r') as file, open(temp_filename, 'w') as temp_file:
        for line in file:
            # Write the current line to the temporary file
            temp_file.write(line)
            # If the line contains the search string, append the new string
            if search_string in line:
                temp_file.write(new_string)
    
    # Replace the original file with the modified content
    import os
    os.remove(filename)
    os.rename(temp_filename, filename)

