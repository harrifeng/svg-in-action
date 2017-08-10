import igraph as ig
from util import get_color_arr
N = 31
g = ig.Graph.Tree(N, 2)
print g

del_nodes = [5, 6]

g.vs['size'] = ['80']
g.vs['color'] = get_color_arr(N)
g.vs['label'] = range(31)
g.vs['label_size'] = ['20']

del_nodes.extend(range(15, 17))
del_nodes.extend(range(21, 31))
del_nodes.extend(range(11, 15))
g.delete_vertices(del_nodes)

g.vs['label'] = ['[]',
                 '[L]', 'quit',
                 '[LL]', '[LR]',
                 'quit', '[LLR]', '[LRL]', 'quit',
                 'quit', '[LLRR]', '[LRLR]', 'quit'
                 ]

layout = g.layout_reingold_tilford(mode="in", root=[0])


g.write_svg('002.svg', layout=layout, vertex_size=20)
ig.plot(g, layout=layout, bbox=(800, 300), margin=50)
