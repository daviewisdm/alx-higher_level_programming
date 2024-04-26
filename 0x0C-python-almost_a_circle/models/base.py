#!/usr/bin/python3
""" Base Class """
import json
import os


class Base:
    """base class to manage id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initiation function of class"""
        if id is not None:
            if type(id) is not int:
                raise TypeError(" id must be int")
            elif id < 0:
                raise ValueError(" id must be positive int")
            else:
                self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if type(list_dictionaries) is not list:
            raise TypeError("input must be list")
        if list_dictionaries and list_dictionaries != []:
            return json.dumps(list_dictionaries)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        if type(list_objs) is not list:
            raise TypeError("input must be list")
        instances_list = []
        if list_objs and list_objs != []:
            class_name = type(
                list_objs[0]
            ).__name__  # or list_objs[0].__class__.__name__

            counter = 0
            obj_num = len(list_objs)
            dic_to_append = {}
            if class_name == "Rectangle":
                att = ["y", "x", "id", "width", "height"]
            elif class_name == "Sqaure":
                att = ["id", "size", "x", "y"]
            for i in range(obj_num):
                for att_name in att:
                    if att_name == "size":
                        dic_to_append[att_name] = getattr(list_objs[counter], "width")
                    dic_to_append[att_name] = getattr(list_objs[counter], att_name)
                instances_list.append(dic_to_append)
                # print(instances_list)
                counter += 1
                if counter == obj_num:
                    break
            # print(instances_list)
            with open("{}.json".format(class_name), "w") as file:
                file.write(Base.to_json_string(instances_list))
        else:
            return instances_list

    @staticmethod
    def from_json_string(json_string):
        if type(json_string) is not str:
            raise TypeError(" inout must be string")
        if json_string and json_string != "":
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        if type(dictionary) is not dict:
            raise TypeError(" inout must be dict")
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new_obj = Rectangle(1, 2)
        elif cls is Square:
            new_obj = Square(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new_obj = Rectangle(1, 2)
        elif cls is Square:
            new_obj = Square(1)
        instances_list = []
        class_name = cls
        if not os.path.exists(f"{class_name}.json"):
            return []
        else:
            with open(f"{class_name}.json", "r") as file:
                json_str = file.read()
            list_from_str = Base.from_json_string(json_str)
            for dic in list_from_str:
                instances_list.append(new_obj.update(dic))
            return instances_list
