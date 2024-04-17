#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys
import json

# Load exist
try:
    with open('add_item.json', 'r') as file:
        items = json.load(file)
except FileNotFoundError:
    items = []

# Add arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to file
with open('add_item.json', 'w') as file:
    json.dump(items, file)
