#!/usr/bin/python3
""" Class Rectangle """
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initiation function of class"""

        if id is not None:
            if not all(isinstance(var, int) for var in (id, width, height, x, y)):
                raise TypeError
            elif id < 0 or width < 0 or height < 0:
                raise ValueError

        for var_name, var_value in {"width": width, "height": height}.items():
            if type(var_value) is not int:
                raise TypeError(f"{var_name} must be an integer")

        for var_name, var_value in [("width", width), ("height", height)]:
            if var_value <= 0:
                raise ValueError(f"{var_name} must be > 0")

        for var_name, var_value in [("x", x), ("y", y)]:
            if var_value < 0:
                raise ValueError(f"{var_name} must be >= 0")

        # for var_name, var_value in {
        # 'width': width, 'height': height}.items():
        #     if var_value <= 0:
        #         raise ValueError(f"{var_name} must be > 0")

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes area"""
        return self.__width * self.__height

    def display(self):
        """draws shape"""
        for y_spaces in range(self.y):
            print()
        for i in range(self.height):
            for x_spaces in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """on printing object or using str() function"""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """updating attributes of the object"""

        if args != ():  # empty tuple
            for arg, (var_name, var_value) in zip(args, self.__dict__.items()):
                setattr(self, var_name, arg)
        else:
            if kwargs and kwargs != {}:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """displays attributes in the form of a dictionary"""
        # method 1
        # return {
        #     'x': self.x,
        #     'y': self.y,
        #     'id': self.id,
        #     'height': self.height,
        #     'width': self.width,
        # } # { inidicate a dic }

        # method 2
        att = ["x", "y", "id", "height", "width"]
        representaion = {}
        for i in range(len(att)):
            if att[i] in self.__dir__():
                representaion[att[i]] = getattr(self, att[i])
                # print(representaion)
        return representaion
