# Day 3

def score(c: str):
    return ord(c) - 38 if c.isupper() else ord(c) - 96


with open('03.input') as f:
    data = f.read()

rows = data.split('\n')
backpacks = [(set(r[:int(len(r) / 2)]), set(r[int(len(r) / 2):])) for r in rows]
intersects = [a & b for a, b in backpacks]
scores = [score(c) for i in intersects for c in i]
print(intersects)
print(scores)
print('Part 1:', sum(scores))

trios = [rows[n:n + 3] for n in range(0, len(backpacks), 3)]
intersects = []
for trio in trios:
    intersects.append(set(trio[0]) & set(trio[1]) & set(trio[2]))
scores = [score(c) for i in intersects for c in i]
print('Part 2:', sum(scores))
