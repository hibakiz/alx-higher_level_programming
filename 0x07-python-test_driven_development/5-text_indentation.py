#!/usr/bin/python3
'''print the name.
    Args:
    text: the string text from the user
    Returns: no returns'''


def text_indentation(text):
    '''indentation removal
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    j = 0
    while j < len(text) and text[j] == " ":
        j += 1

    while j < len(text):
        print(text[j], end="")
        if text[j] in ".:?" or text[j] == '\n':
            if text[j] in ".:?":
                print("\n")
            j += 1
            while j < len(text) and text[j] == " ":
                j += 1
            continue
        j += 1
