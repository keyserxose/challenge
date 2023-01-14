#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from urllib.request import urlopen

# Reading from the current path
path = __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

global url
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

count = 0

global pattern
pattern = '[0-9]'

def getNextURL(numURL):
    global nextURL
    global decoded_body
    global count
    response = urlopen(url+numURL)
    print("Current URL: "+url+numURL)
    body = response.read()
    decoded_body = body.decode("utf-8")
    print(decoded_body)
    myPattern = re.findall(pattern, decoded_body)
    nextURL = ''.join(myPattern)
    print(nextURL)
    count += 1
    print(count)
    response.close()


getNextURL('12345')
while count < 400:
    file = open('log.txt', 'a')
    getNextURL(nextURL)
    file.write(decoded_body+'\n')
    file.close()


# url: http://www.pythonchallenge.com/pc/def/linkedlist.php