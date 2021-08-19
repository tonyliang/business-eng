#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

with open('./11-20/data.txt', 'r', encoding='utf-8') as outfile:
    d = json.load(outfile)
    print(d[0]['en'])
    print(d[0]['zh'])
    print(d[60])
