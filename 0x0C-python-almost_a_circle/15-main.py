#!/usr/bin/python3
""" 15-main """
from models.square import Square
import os
import json

if __name__ == "__main__":

    r1 = Square(5, 0, 0, 346)
    Square.save_to_file([r1])

    with open("Square.json", "r") as file:
        content = file.read()
   
    print(json.loads(content))
