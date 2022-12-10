# Day 9

import time


def print_grid(knots, w=0, h=0, animate=True):
    if not w or not h:
        return
    print(f'{h}:{w} Grid')
    for y in range(h):
        for x in range(w):
            c = '.'
            for k, i in zip(knots, range(len(knots))):
                if k[0] == x and h - 1 - k[1] == y:
                    c = f'{i if i<10 else "X"}'
            print(c, end='')
        print('\n', end='')
    if animate:
        print(f'\033[{h + 2}A')
        time.sleep(.2)


def follow(t, h):
    if all([t[i] - 1 <= h[i] <= t[i] + 1 for i in range(2)]):
        return t
    (tail_x, tail_y), (head_x, head_y) = t, h
    if tail_x == head_x:
        t[1] += int(tail_y < head_y) * 2 - 1
    elif tail_y == head_y:
        t[0] += int(tail_x < head_x) * 2 - 1
    else:
        t[0] += int(tail_x < head_x) * 2 - 1
        t[1] += int(tail_y < head_y) * 2 - 1
    return t

def run(knots, w, h):
    Tpos = [(0, 0)]
    print_grid(knots, w, h)
    for direction, steps in movements:
        for step in range(steps):
            if direction == R:
                knots[0][0] += 1
            if direction == L:
                knots[0][0] -= 1
            if direction == U:
                knots[0][1] += 1
            if direction == D:
                knots[0][1] -= 1

            for i in range(len(knots)-1):
                knots[i + 1] = follow(knots[i+1], knots[i])


            Tpos.append((knots[-1][0], knots[-1][1]))
            print(knots)
            print_grid(knots, w, h)
    return Tpos

with open('09.input') as f:
    data = [tuple(r.split(' ')) for r in f.read().split('\n') if r]

movements = [(d, int(s)) for d, s in data]
R = 'R'
U = 'U'
L = 'L'
D = 'D'

# Useless for actual data. Use 10, 10 for example data
w = 0
h = 0

knots = [[0, 0] for i in range(2)]
Tpos = run(knots, 6, 6)
Tset = set(Tpos)
print('Part 1:', len(Tset))

knots = [[0, 0] for i in range(10)]
Tpos = run(knots, w, h)
Tset = set(Tpos)
print(Tset)
print_grid(Tpos, w, h, animate=False)
print('Part 2:', len(Tset))
