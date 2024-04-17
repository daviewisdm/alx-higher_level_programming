#!/usr/bin/python3
"""from JSON string to Object"""


import json


def from_json_string(my_str):
    """returns an object"""
    return json.loads(my_str)
