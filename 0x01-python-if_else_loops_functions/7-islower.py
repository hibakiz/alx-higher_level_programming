#!/usr/bin/env python3
def islower(c):
    for i in range (97, 123):
        if c == chr(i):
            return True

    return False