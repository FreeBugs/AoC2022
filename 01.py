# Day 1

with open('01.input') as f:
    data = f.read()

chunks = [[int(cals) for cals in group.split('\n')] for group in data.split('\n\n')]
sums = sorted([sum(cals) for cals in chunks], reverse=False)
print('Top elf:', sums[-1])
print('Top 3 elves:', sum(sums[-3:]))
