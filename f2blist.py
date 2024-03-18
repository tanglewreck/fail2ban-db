#!/usr/bin/env python3

import json

with open("fail2ban.banned") as f2b:
    f2b_json = json.load(f2b)
for item in f2b_json:
    key = list(item.keys())[0]
    if key == 'postfix':
        for ip in list(item.values())[0]:
            print(ip)

