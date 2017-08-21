import igraph as ig
from util import get_color_arr

N = 40
g = ig.Graph.Tree(N, 3)
layout = g.layout_reingold_tilford(mode="in", root=[0])
g.vs['size'] = ['20']
g.vs['color'] = get_color_arr(N, 3)

# del_nodes = [6]
del_nodes = []

g.vs['label'] = ['[1, 2, 3]',
                 '[1, 2, 3]', '[2, 1, 3]', '[3, 2, 1]',
                 '[1, 2, 3]', '[1, 3, 2]', '[]',
                 '[2, 1, 3]', '[2, 3, 1]', '[]',
                 '[3, 2, 1]', '[3, 1, 2]', '[]']
g.vs['label'] = range(N)
g.vs['label_size'] = ['20']

g.delete_vertices(del_nodes)

g.write_svg('001.svg', layout=layout, vertex_size=20)
ig.plot(g, layout=layout, bbox=(800, 300), margin=50)
