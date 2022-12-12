# Day 11
import copy
import math
import re
from tqdm import tqdm
from math import prod

with open('11.input') as f:
    raw_monkey = [m.split('\n') for m in f.read().split('\n\n')]

class Monkey:
    def __init__(self, id, items, operation, test, if_true, if_false):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.count = 0

    def has_items(self):
        return len(self.items) > 0

    def __repr__(self):
        return f'Monkey {self.id} has items: {self.items}' #\nOperation: {self.operation}\nTest: {self.test}: True: {self.if_true}, False: {self.if_false}'

def print_monkeys(the_monkeys):
    for m in the_monkeys:
        print(m)

def monkey_business(the_monkeys, mod=None):
    for m in the_monkeys:
        while m.has_items():
            m.count += 1
            old = str(m.items.pop())
            fun = m.operation.replace('old', old)
            new = eval(fun)
            if not mod:
                new //= 3
            else:
                new %= mod
            test = new % m.test == 0
            target = m.if_true if test else m.if_false
            the_monkeys[target].items.append(new)
    return the_monkeys


monkeys = []
for m, mi in zip(raw_monkey, range(len(raw_monkey))):
    monkeys.append(Monkey(
        id = mi,
        items = [int(i) for i in re.match(r'\s*Starting items: (.*)', m[1]).group(1).split(', ')],
        operation = re.match(r'\s*Operation: new = (.*)', m[2]).group(1),
        test= int(re.match(r'\s*Test: divisible by (.*)', m[3]).group(1)),
        if_true= int(re.match(r'\s*If true: throw to monkey (.*)', m[4]).group(1)),
        if_false= int(re.match(r'\s*If false: throw to monkey (.*)', m[5]).group(1)),
    ))


lcm = math.lcm(*[m.test for m in monkeys])

part2_monkeys = copy.deepcopy(monkeys) # Save fresh monkeys for later

for i in tqdm(range(20)):
    monkeys = monkey_business(monkeys)

for i in tqdm(range(10000)):
    part2_monkeys = monkey_business(part2_monkeys, lcm)

print('Part 1: ', prod(sorted([m.count for m in monkeys])[-2:]))
print('Part 2: ', prod(sorted([m.count for m in part2_monkeys])[-2:]))
