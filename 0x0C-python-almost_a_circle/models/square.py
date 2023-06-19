#!/usr/bin/python3
"""the quare module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """the init func"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the tostring implementation"""
        a = "[Square] "
        b = str(self.id)
        c = str(self.x)
        d = str(self.y)
        e = str(self.width)
        return (a + "(" + b + ")" + " " + c + "/" + d + " - " + e)

    @property
    def size(self):
        """return size"""
        return (self.width)

    @size.setter
    def size(self, size):
        """the setter for size"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update the attributes"""
        status = 0
        if type(args) != tuple or len(args) == 0:
            for i in list(kwargs.items()):
                if i[0] == "size":
                    self.width = i[1]
                    self.height = i[1]
                if i[0] == "id":
                    self.id = i[1]
                if i[0] == "x":
                    self.x = i[1]
                if i[0] == "y":
                    self.y = i[1]
            return
        for j in args:
            if status == 0:
                self.id = j
            if status == 1:
                self.width = j
                self.height = j
            if status == 2:
                self.x = j
            if status == 4:
                self.y = j
            status += 1

    def to_dictionary(self):
        """get dict representation of class"""
        new = {}
        fr = new.fromkeys(["id", "size", "x", "y"])
        for h in list(self.__dict__.items()):
            if h[0] == "id":
                fr.update({"id": h[1]})
            if h[0] == "_Rectangle__width":
                fr.update({"size": h[1]})
            if h[0] == "_Rectangle__height":
                fr.update({"size": h[1]})
            if h[0] == "_Rectangle__x":
                fr.update({"x": h[1]})
            if h[0] == "_Rectangle__y":
                fr.update({"y": h[1]})
        return (fr)
