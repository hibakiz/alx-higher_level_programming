#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
            print("{}".format(chr(ord(str[i]) - 32) if ord(str[i]) >= 97 and ord(str[i]) <=122 else str[i]), end="")
    print()
       # else:
  #          print("{}".format(str[i]), end="")
 #
    return
