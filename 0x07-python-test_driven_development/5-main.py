#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

def checker(text=""):
    try:
        text_indentation(text)
    except Exception as e:
        print (e)
