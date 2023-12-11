#!/usr/bin/python3
"""Suare module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """inint function"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Size Getter"""
        return self.__width

    @size.setter
    def size(self, size):
        """Size settrt"""
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__width = size
        self.__height = size

    def __str__(self):
        """Update the str function"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    # The updtae function
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
            for i in range(len(args)):
                if i == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    # to dictionary
    def to_dictionary(self):
        """retrun the dictionary of a Rectangle"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
