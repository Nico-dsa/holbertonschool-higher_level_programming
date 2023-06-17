#!/usr/bin/python3
def text_indentation(text):
	'''Write a function that prints a text with 2 new lines \
	after each of these characters: ., ? and :'''
    caractere = [".", "?", ":"]
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = 0
    for i in text:
        if x == 0:
            if i == ' ':
                continue
            else:
                x = 1

        if x == 1:
            if i in ".?:":
                print(i + '\n')
                x = 0
            else:
                print(i, end='')
