#!/usr/bin/python3
"""the base module"""
import json
import csv
import turtle


class Base:
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the init func"""
        if id is not None:
            self.id  = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        """convert to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    def save_to_file(list_objs):
        """save json rep to a file"""
        lis = []
        if len(list_objs) > 0:
            for k in list_objs:
                lis.append(k.to_dictionary())
            with open(list_objs[0].__class__.__name__ + ".json", 'w') as fle:
                fle.write(Base.to_json_string(lis))
        else:
            return (lis)
        
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """create and update an object"""
        if cls.__name__ == "Rectangle":
            rectangle = cls(10, 10, 10, 10)
            rectangle.update(**dictionary)
            return (rectangle)
        if cls.__name__ == "Square":
            square = cls(10)
            square.update(**dictionary)
            return (square)

    @classmethod
    def load_from_file(cls):
        """load instances list"""
        if cls.__name__ == "Rectangle":
            try:
                lis = []
                with open("Rectangle.json", 'r') as fle:
                    content = fle.read()
                    for aitch in json.loads(content):
                        br = cls.create(**aitch)
                        lis.append(br)
                    return (lis)
            except FileExistsError:
                return ([])
        if cls.__name__ == "Square":
            try:
                ty = []
                with open("Square.json", 'r') as fle:
                    content = fle.read()
                    print("content")
                    for ai in json.loads(content):
                        br = cls.create(**ai)
                        ty.append(br)
                    return (ty)
            except FileExistsError:
                return ([])
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """dealing with csv"""
        pr = []
        with open(cls.__name__ + ".csv", 'w') as fle:
            wr = csv.writer(fle)
            pr.append(list_objs)
            wr.writerows(pr)

    @classmethod
    def load_from_file_csv(cls):
        """the loadeer of the sv from file"""
        if cls.__name__ == "Rectangle":
            with open("Rectangle.csv", 'r') as fle:
                rd = csv.reader(fle)
                for j in rd:
                    return (j)
        if cls.__name__ == "Square":
            with open("Square.csv", 'r') as fl:
                rs = csv.reader(fl)
                for h in rs:
                    return (h)
    def draw(list_rectangles, list_squares):
        """to draw thw circle"""
        ti = turtle.TK.Tk()
        ti.title("Display Window")
        ti.geometry("400x300")
