#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file_n = file.write(text)
    return file_n
