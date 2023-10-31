#!/usr/bin/python3
i = 97
for i in range(97, 123):
    if i == 101 or i == 113:
        pass
    else:
        print("{}".format("".join(chr(i))), end="")
