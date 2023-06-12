#!/usr/bin/python3
""" a class BaseGeometry (based on 6-base_geometry"""


class BaseGeometry:
    """a class BaseGeometry"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
