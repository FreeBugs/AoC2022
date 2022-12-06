# Day 5
import copy
import re
from textwrap import wrap

with open('05.input') as f:
    data = f.read().split('\n')

empty_row = 0
for empty_row in range(0, len(data)):
    if data[empty_row] == '':
        break

stack_data = [[re.sub(r'[\[\]\s]', '', e) for e in wrap(r, width=4, drop_whitespace=False)] for r in
              list(reversed(data[:empty_row]))]
n_stacks = len(stack_data[0])
stacks = [[] for _ in range(n_stacks)]
for row in stack_data[1:]:
    for i in range(len(row)):
        if len(row[i]) > 0:
            stacks[i].append(row[i])

operation_data = data[empty_row + 1:]
operations = [[int(e) for e
               in re.match(r'^move (\d+) from (\d+) to (\d+)$', s).groups()] for s in operation_data]

work_stacks = copy.deepcopy(stacks)
for op in operations:
    for i in range(op[0]):
        e = work_stacks[op[1] - 1].pop()
        work_stacks[op[2] - 1].append(e)

result = ''.join([e[-1] for e in work_stacks])
print('Part 1:', result)

work_stacks = copy.deepcopy(stacks)
for op in operations:
    e = work_stacks[op[1] - 1][-op[0]:]
    work_stacks[op[1] - 1] = work_stacks[op[1] - 1][:len(work_stacks[op[1] - 1]) - op[0]]
    work_stacks[op[2] - 1].extend(e)

result = ''.join([e[-1] for e in work_stacks])
print('Part 2:', result)
