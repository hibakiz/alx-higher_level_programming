#!/usr/bin/python3
""" read file module"""


def read_file(filename=""):
	'''read file function
	Args:
		filename
	'''
	with open(filename, 'r') as f:
		print(f.read(), end="")
