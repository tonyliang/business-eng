#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

file_name = "./combined/batch1_2_3.txt"
output_name = "./combined/batch1_2_3-out.txt"

def is_eng(code):
    return 65 <= code <= 122

def dump_me(jdata):
    with open(output_name, 'w') as outfile:
        json.dump(jdata, outfile)

rows = []


f = open(file_name)
cur = {"en":"", "zh":""}
for line in f:
    if not len(line) or len(line) < 10:
        continue
    a_code = ord(line[0])
    line = line.strip()
    if is_eng(a_code):
        cur["en"] = line
    else:
        cur['zh'] = line
        rows.append(cur)
        cur = {"en":"", "zh":""}
dump_me(rows)

# print(rows[0]['en'])
# print(rows[0]['zh'].decode('utf-8'))
    

f.close()
