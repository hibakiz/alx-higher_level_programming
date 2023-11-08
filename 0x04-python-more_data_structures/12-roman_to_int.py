#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        units = {'I': 1, 'V': 5, 'X': 10}
        units.update({'L': 50, 'C': 100,  'D': 500, 'M': 100})
        summ = 0
        strr = ''.join(reversed(roman_string))
        for i in range(0, len(strr)):
            if units.get(strr[i]):
                if i == 0:
                    summ += units.get(strr[i])
                else:
                    if units.get(strr[i - 1]) > units.get(strr[i]):
                        summ -= units.get(strr[i])
                    else:
                        summ += units.get(strr[i])
    return (summ)
