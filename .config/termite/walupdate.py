#!/usr/bin/env python3
from pathlib import Path

w = open(str(Path.home())+'/.cache/wal/colors', 'r') 
colorlines = ["color"+str(num) + " = " + x for num,x in enumerate(w.readlines())]
w.close()

c = open('config', 'r')
configlines = c.readlines()[:-16] + colorlines
c.close()

c = open('config', 'w')
for line in configlines:
	c.write(line)
c.close()
