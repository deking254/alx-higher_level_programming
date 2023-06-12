#!/usr/bin/python3
"""a module with a class that inherits int"""


class MyInt(int):
    """the class that implements in"""

    def __eq__(self, number):
        """override this method to negate =="""
        return not super().__eq__(number)

    def __ne__(self, number):
        """override this method to negate !="""
        return not super().__ne__(number)
