#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """a function that reads a text file"""
    with open(filename, encoding="utf-8") as f:
        for i in f:
            print(i, end='')
