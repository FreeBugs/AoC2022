# Day 4

import re

with open('04.input') as f:
    data = f.read()

rows = data.split('\n')
pairs = [re.split(r'[-,]', r) for r in rows]

included = [(int(e[0]) >= int(e[2]) and int(e[1]) <= int(e[3])) or (int(e[0]) <= int(e[2]) and int(e[1]) >= int(e[3]))
            for e in pairs]
print('Part 1:', sum(included))

included = [(int(e[2]) <= int(e[0]) <= int(e[3])) or (int(e[0]) <= int(e[2]) <= int(e[1]))
            for e in pairs]
print('Part 2:', sum(included))
