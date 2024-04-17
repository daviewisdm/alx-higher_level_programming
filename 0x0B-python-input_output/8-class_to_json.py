#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    if isinstance(obj, (list, int, dict, str, bool)):
        return obj
    elif isinstance(obj, (tuple, set)):
        return list(obj)
    elif hasattr(obj, '__dict__'):
        return {key: class_to_json(value)
                for key, value in obj.__dict__.items()}
    else:
        return str(obj)
