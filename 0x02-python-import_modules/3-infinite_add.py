#!/usr/bin/python3

a = 10
b = 5
sum = 0
if __name__ == "__main__":
	from sys import argv
	for i in range(1, len(argv)):
		sum += int(argv[i])
	print("{:d}".format(sum))
