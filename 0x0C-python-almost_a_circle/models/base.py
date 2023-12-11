#!/usr/bin/python3
"""Base class module """

import json


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

	#to json function as static
	@staticmethod
	def to_json_string(list_dictionaries):
		"""Convert to json string function"""
		if list_dictionaries is None or len(list_dictionaries) < 2:
			return "[]"
		return json.dumps(list_dictionaries)

	#save to json file function
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
