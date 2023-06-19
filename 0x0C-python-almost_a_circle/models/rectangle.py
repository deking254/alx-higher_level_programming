#!/usr/bin/python3
"""the rectangle module"""
from models.base import Base


class Rectangle(Base):
    """the rectangle class"""
    __width = None
    __height = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        """the init func"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """the width getter"""
        return (self.__width)

    @width.setter
    def width(self, width=None):
        """the width setter"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        else:
            if width <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width

    @property
    def height(self):
        """the width getter"""
        return (self.__height)

    @height.setter
    def height(self, height=None):
        """the width setter"""
        """the width setter"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        else:
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height

    @property
    def x(self):
        """the width getter"""
        return (self.__x)

    @x.setter
    def x(self, x=None):
        """the width setter"""
        """the width setter"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        else:
            if x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = x

    @property
    def y(self):
        """the width getter"""
        return (self.__y)

    @y.setter
    def y(self, y=None):
        """the width setter"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        else:
            if y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = y

    def area(self):
        """this is th func to calc the rect area"""
        return (self.__height * self.__width)

    def display(self):
        """show the rect in #"""
        for _ in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """used to customize message"""
        a = str(self.id)
        b = str(self.__width)
        c = str(self.__height)
        d = str(self.__x)
        e = str(self.__y)
        f = "[Rectangle] "
        return (f + "(" + a + ")" + " " + d + "/" + e + " - " + b + "/" + c)

    def update(self, *args, **kwargs):
        """update the attributes"""
        status = 0
        if type(args) != tuple or len(args) == 0:
            index = 0
            for i in list(kwargs.items()):
                if i[0] == "width":
                    self.width = i[1]
                if i[0] == "height":
                    self.height = i[1]
                if i[0] == "x":
                    self.x = i[1]
                if i[0] == "y":
                    self.y = i[1]
                if i[0] == "id":
                    self.id = i[1]
            return
        for j in args:
            if status == 0:
                self.id = j
            if status == 1:
                self.width = j
            if status == 2:
                self.height = j
            if status == 3:
                self.x = j
            if status == 4:
                self.y = j
            status += 1

    def to_dictionary(self):
        """get dict representation of class"""
        new = {}
        fr = new.fromkeys(["id", "width", "height", "x", "y"])
        for h in list(self.__dict__.items()):
            if h[0] == "id":
                fr.update({"id": h[1]})
            if h[0] == "_Rectangle__width":
                fr.update({"width": h[1]})
            if h[0] == "_Rectangle__height":
                fr.update({"height": h[1]})
            if h[0] == "_Rectangle__x":
                fr.update({"x": h[1]})
            if h[0] == "_Rectangle__y":
                fr.update({"y": h[1]})
        return (fr)
