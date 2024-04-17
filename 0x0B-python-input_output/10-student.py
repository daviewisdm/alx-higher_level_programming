#!/usr/bin/python3
"""student to json with filter"""


class Student:
    """define a class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        student_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                student_dict[attr] = self.__dict__[attr]
        return student_dict
