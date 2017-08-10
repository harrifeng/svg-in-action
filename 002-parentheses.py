import igraph as ig
from util import get_color_arr
N = 31
g = ig.Graph.Tree(N, 2)
print g
g.delete_vertices(range(23, 31))
g.delete_vertices(range(11, 15))
g.delete_vertices([2, 5, 6])

layout = g.layout_reingold_tilford(mode="in", root=[0])
g.vs['size'] = ['60']
g.vs['color'] = get_color_arr(N)
g.vs['label'] = range(31)
g.vs['label_size'] = ['20']

g.write_svg('002.svg', layout=layout, vertex_size=20)
ig.plot(g, layout=layout, bbox=(800, 300), margin=50)
