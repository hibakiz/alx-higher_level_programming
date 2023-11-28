#!/usr/bin/python3
def magic_string():
    magic_string.count = magic_string.__dict__.setdefault('count', 0) + 1
    return ', '.join(f"{'BestSchool'}" for i in range(magic_string.count))
