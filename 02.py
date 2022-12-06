# Day 2

with open('02.input') as f:
    data = f.read()
rows = data.replace(' ', '').split('\n')

wins = 6
lose = 0
draw = 3
outcomes = {'AX': 1 + draw, 'AY': 2 + wins, 'AZ': 3 + lose,
            'BX': 1 + lose, 'BY': 2 + draw, 'BZ': 3 + wins,
            'CX': 1 + wins, 'CY': 2 + lose, 'CZ': 3 + draw}
scores = [outcomes[o] for o in rows]
print('Part 1:', sum(scores))

choices = {'AX': 'AZ', 'AY': 'AX', 'AZ': 'AY',
           'BX': 'BX', 'BY': 'BY', 'BZ': 'BZ',
           'CX': 'CY', 'CY': 'CZ', 'CZ': 'CX'}
scores = [outcomes[choices[o]] for o in rows]
print('Part 2:', sum(scores))
