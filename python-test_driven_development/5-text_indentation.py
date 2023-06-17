#!/usr/bin/python3
"""Text indentation"""



def text_indentation(text):
	'''Write a function that prints a text with 2 new lines \
	after each of these characters: ., ? and :'''
    if type(text) is not str:
    	raise TypeError("text must be a string")

    string = text.replace('.', '.\n\n').replace(':', ':\n\n')\
    .replace('?', '?\n\n')
    for i in range (len(str)):
    	string = string.replace('\n ', '\n')

    print(string, end='')
