#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pickle
from PIL import Image
import numpy as np
import io

# Reading from the current path
path = __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))



# url: http://www.pythonchallenge.com/pc/def/peak.html




file = open('banner.p', 'r')
#file = open('peakhell.jpg', 'r')
data = file.read()

# Read Image 
#byteImgIO = io.BytesIO()
#byteImg = Image.open('banner.p')
#byteImg.save(byteImgIO, "PNG")
#byteImgIO.seek(0)
#byteImg = byteImgIO.read()
#print(byteImg)


my_object = data

my_pickled_object = pickle.dumps(my_object)  # Pickling the object
print(f"This is my pickled object:\n{my_pickled_object}\n")

#file = open('output.txt', 'a')
#file.write(my_pickled_object)
#file.close()


my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
#print(f"This is a_dict of the unpickled object:\n{my_unpickled_object}\n")