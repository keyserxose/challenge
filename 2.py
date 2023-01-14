#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
from collections import Counter
from urllib.request import urlopen

# Reading from the current path
path = __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

mess = open(path+'/2.txt','r')
data = mess.read()


c = Counter(data)
li = c.most_common()
print(li)


#equality

# url: http://www.pythonchallenge.com/pc/def/ocr.html