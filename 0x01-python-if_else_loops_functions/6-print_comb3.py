#!/usr/bin/python3
i = 0 
j = 1

    
print(", ".join(["{}{}".format(min(i, j), max(i, j))  for j in range(i + 1, 10) for i in range(9) if i != j]))
