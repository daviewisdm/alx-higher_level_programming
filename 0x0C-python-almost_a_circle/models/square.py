#!/usr/bin/python3
""" Sqaure Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Sqaure the Inherts Rectangle class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialization function """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value  # super(),.width(value)
        self.height = value

    def update(self, *args, **kwargs):
        """ update value of attributes of an objject """
        if args and args != ():
            attributes = ["id", "size", "x", "y"]
            counter = 0
            for arg in args:
                if counter == 1:
                    self.width = arg
                    self.height = arg
                    counter += 1
                    # print(attributes[counter])
                    # print(" updtaed siize counter now is {}".format(counter))
                else:
                    # print(attributes[counter])
                    setattr(self, attributes[counter], arg)
                    counter += 1
                    # print(" updtaed att counter now is {}".format(counter))
        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ displays attributes in the form of dictionary """
        # method 1
        # return {
        #     'x': self.x,
        #     'y': self.y,
        #     'id': self.id,
        #     'size': self.height
        # } # { inidicate a dic

        # method 2
        att = ["id", "size", "x", "y"]
        representaion = {}
        for i in range(len(att)):
            if i == 1:
                representaion[att[i]] = getattr(self, "width")
            else:
                if att[i] in self.__dir__():
                    representaion[att[i]] = getattr(self, att[i])
        return representaion
