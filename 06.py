# Day 6

with open('06.input') as f:
    data = f.read().split('\n')


def process(s, part, n_unique):
    found_at = None
    for i in range(len(s) - n_unique):
        s1 = s[i:i + n_unique]
        if len(set(s1)) == n_unique:
            found_at = i
            break
    print(f'Part {part}:', found_at + n_unique if found_at else '-')


for line in data:
    process(line, 1, 4)

for line in data:
    process(line, 2, 14)
