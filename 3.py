#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os

# Reading from the current path
path = __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

mess = open(path+'/3.txt','r')
data = mess.read()

pattern = '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'

# Function to match the string
def match(text):
        myPattern = re.findall(pattern, text)
        if myPattern:
            print(myPattern)
            print('Yes')
            return('Yes')
        else:
            return('No')

match(data)

# url: http://www.pythonchallenge.com/pc/def/equality.html