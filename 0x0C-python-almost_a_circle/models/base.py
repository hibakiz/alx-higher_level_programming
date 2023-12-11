#!/usr/bin/python3
"""Base class module """

import json
import os
import csv
import turtle


class Base:
    """ the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    # to json function as static
    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert to json string function"""
        if list_dictionaries is None or len(list_dictionaries) < 2:
            return "[]"
        return json.dumps(list_dictionaries)

    # save to json file function
    @classmethod
    def save_to_file(cls, list_objs):
        """Save the data to json file"""
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                f.write(cls.to_json_string(list_dicts))

    # from json to string function
    @staticmethod
    def from_json_string(json_string):
        """convert from json to string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    # create function
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    # load from file function
    @classmethod
    def load_from_file(cls):
        """load the data from a file"""
        filename = f"{cls.__name__}.json"
        list_instance = []
        list_doc = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                strr = f.read()
                list_doc = cls.from_json_string(strr)
                for dicti in list_doc:
                    list_instance.append(cls.create(**dicti))
        return list_instance

    # save JSON but CSV
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to a json file as csv format"""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline="") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]
                else:
                    fields = ["id", "width", "height", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    # load from JSON but CSV
    @classmethod
    def load_from_file_csv(cls):
        """load from  json file as csv format"""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    # Draw the square and rectangles
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#000000")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#ADD8E6")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
