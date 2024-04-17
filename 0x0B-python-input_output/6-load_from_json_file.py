#!/usr/bin/python3
"""Create object from a JSON file"""


import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename, 'r', encoding='utf-8') as file:
        x = json.load(file)
    return x
