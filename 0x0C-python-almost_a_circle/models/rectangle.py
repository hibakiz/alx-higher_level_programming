#!/usr/bin/python3
""" Rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init function"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # The width setter and getter
    @property
    def width(self):
        """getter"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    # The height getter and setter
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    # The x getter and setter
    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    # The y getter and setter
    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    # The Area function
    def area(self):
        """ return the area for the rectangle"""
        return self.width * self.height

    # The print Rectangle function
    def display(self):
        """ print the rectangle using #"""
        for k in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    # The __str__ function
    def __str__(self):
        """ override the str method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} "
        f"- {self.width}/{self.height}"

    # The updtae function
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[0]
                elif i == 1:
                    self.width = args[1]
                elif i == 2:
                    self.height = args[2]
                elif i == 3:
                    self.x = args[3]
                elif i == 4:
                    self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    # to dictionary
    def to_dictionary(self):
        """retrun the dictionary of a Rectangle"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
