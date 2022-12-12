# Day 12

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def get_adjacent_indices(i, j, shape):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i - 1, j))
    if i + 1 < shape[0]:
        adjacent_indices.append((i + 1, j))
    if j > 0:
        adjacent_indices.append((i, j - 1))
    if j + 1 < shape[1]:
        adjacent_indices.append((i, j + 1))
    return adjacent_indices


def get_cell_index(i, j, shape):
    return i * shape[1] + j


def get_cell_index_a(a, shape):
    return a[0] * shape[1] + a[1]


with open('12.input') as f:
    data = np.array([[ord(v) for v in s] for s in f.read().split('\n')])

c = tuple(np.argwhere(data == ord('S'))[0])
data[c] = ord('a')
start_pos = get_cell_index_a(c, data.shape)
c = tuple(np.argwhere(data == ord('E'))[0])
data[c] = ord('z')
dest_pos = get_cell_index_a(c, data.shape)

edges = []
colors = []
pos = {}
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        idx = get_cell_index(i, j, data.shape)
        pos[idx] = [j, data.shape[1] - i]
        if idx == start_pos:
            colors.append('orange')
        elif idx == dest_pos:
            colors.append('green')
        else:
            colors.append('lightgray')
        for adj_i, adj_j in get_adjacent_indices(i, j, data.shape):
            height_diff = data[adj_i, adj_j] - data[i, j]
            if height_diff <= 1:
                edges.append((
                    get_cell_index(i, j, data.shape),
                    get_cell_index(adj_i, adj_j, data.shape)
                ))

G = nx.DiGraph()
for i in range(data.shape[0] * data.shape[1]):
    G.add_node(i)
G.add_edges_from(edges)

p = nx.shortest_path(G, source=start_pos, target=dest_pos)

ax = plt.figure().gca()
ax.set_axis_off()
ax = plt.figure(figsize=(30, 15), dpi=200).gca()
ax.set_axis_off()
options = {'node_size': 4,
           'node_color': colors,
           'edge_color': 'lightgray',
           'arrowsize': 4}
nx.draw(G, pos, with_labels=False, arrows=False, **options)
p_list = [(p[i], p[i + 1]) for i in range(len(p) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=p_list, edge_color='r', width=2, node_size=5)
plt.show()

print('Part 1:', len(p))

all_the_a = [get_cell_index_a(e, data.shape) for e in np.argwhere(data == ord('a'))]
p_len, _ = nx.multi_source_dijkstra(G, all_the_a, dest_pos)

print('Part 2:', p_len)
