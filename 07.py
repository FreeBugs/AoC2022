# Day 7

import re

with open('07.input') as f:
    data = f.read().split('\n')


class Node:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = []
        self.size:int = 0

    def __str__(self):
        return self.name

    def traverse(self, log_output: list[str], line) -> int:
        while line < len(log_output):
            # print('Parse: ', log_output[line])
            if log_output[line] == '$ cd ..':
                break
            if log_output[line].startswith('$ cd '):
                n = Node(log_output[line][5:])
                line = n.traverse(log_output, line + 1)
                self.dirs.append(n)
            else:
                m = re.match(r'^(?P<size>\d+)\s(?P<fname>.+)$', log_output[line])
                if m:
                    self.files.append((int(m['size']), m['fname']))
            line += 1
        self.size = sum([d.size for d in self.dirs]) + sum([f[0] for f in self.files])
        return line

    def get_dirs_by_size(self, max_size = None, min_size = None) -> list[(int, str)]:
        res = []
        for d in self.dirs:
            res.extend(d.get_dirs_by_size(max_size=max_size, min_size=min_size))
        if max_size and self.size <= max_size:
            res.append((self.size, self.name))
        if min_size and self.size >= min_size:
            res.append((self.size, self.name))
        return res

    def display(self, indent=0):
        print(f'{"| " * indent}|--- {self.name} ({self.size})')
        for d in self.dirs:
            d.display(indent + 1)
        for size, fname in self.files:
            print(f'{"| " * indent}|--- {fname} ({size})')


root = Node('/')
root.traverse(data, 1)
# root.display()

dirs_of_interest = root.get_dirs_by_size(max_size=100000)
print('Part 1:', sum([d[0] for d in dirs_of_interest]))

capacity = 70000000
required = 30000000
free_up = required - (capacity - root.size)
dirs_of_interest = root.get_dirs_by_size(min_size=free_up)
smallest = sorted(dirs_of_interest)[0]
print('Part 2:', smallest[0])