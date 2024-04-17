#!/usr/bin/python3
def add_attribute(obj, attr_name, attr_value):
    # Check if the object is an instance of a class that allows adding new attributes
    if not isinstance(obj, (type, types.ModuleType)):
        # Use setattr to add the new attribute to the object
        setattr(obj, attr_name, attr_value)
    else:
        # If the object does not allow adding new attributes, raise a TypeError
        raise TypeError("can't add new attribute")

