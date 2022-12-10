# Day 8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_it(arr, x, y):
    width, height = arr.shape
    fig = plt.figure(figsize=(10, 10))
    X, Y = np.meshgrid(range(width), range(height))
    plt_data = arr.ravel()
    bottom = np.zeros_like(plt_data)
    width = depth = .3
    cmap = cm.get_cmap('Greens')
    max_height = np.max(plt_data)
    min_height = np.min(plt_data)
    c = [cmap((k - min_height) / max_height) for k in plt_data]
    ax = fig.add_subplot(111, projection='3d')
    ax.bar3d(X.ravel(), Y.ravel(), bottom, width, depth, plt_data,
             shade=True, color=c, antialiased=True)
    ax.text(x, y, arr[y, x], 'x', fontsize=20)
    plt.show()


def axis_projection(vec: np.ndarray, start=-9, from_tree=False) -> np.ndarray:
    h = -9
    res = np.zeros_like(vec, dtype=bool)
    for i, e in np.ndenumerate(vec):
        if from_tree:
            res[i] = True
            if e >= start:
                res[i] = True
                return res
        elif e > h:
            res[i] = True
            h = e
    return res


with open('08.input') as f:
    data = [[int(t) for t in r] for r in f.read().split('\n') if r]

a = np.array(data, dtype=int)

vis = np.zeros_like(a, dtype=bool)
for view_direction in range(4):
    v = np.rot90(a, view_direction)
    p = np.apply_along_axis(axis_projection, 0, v)
    p = np.rot90(p, -view_direction)
    vis = np.logical_or(vis, p)
print('Part 1:', np.sum(vis))

high_score = 0
for y in list(range(a.shape[0])):
    for x in list(range(a.shape[1])):
        directions = [
            np.flip(a[y, :x]),
            a[y, x + 1:],
            np.flip(a[:y, x]),
            a[y + 1:, x]
        ]
        vis = np.array([np.sum(axis_projection(d, start=a[y, x], from_tree=True)) for d in directions if len(d) > 0])
        score = np.prod(vis)
        if score > high_score:
            high_score = score
            home_x = x
            home_y = y
print('Part 2:', high_score)
plot_it(a, home_x, home_y)