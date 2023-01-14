#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import requests
import string
from itertools import cycle


input_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alphabet = list(string.ascii_lowercase)
print(alphabet)

li = []

for c in input_string:
    if c in alphabet:
        try:
            find_item = (alphabet.index(c) + 2) %26
            li.append(alphabet[find_item])
        except (IndexError, ValueError):
            pass
    else:
        li.append(c)

ans = ' '
for i in li:
    ans = ans+ ''+ i
print(ans)

# url: http://www.pythonchallenge.com/pc/def/map.html