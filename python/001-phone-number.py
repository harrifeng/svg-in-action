import igraph as ig
from util import get_color_arr

N = 13
g = ig.Graph.Tree(N, 3)
layout = g.layout_reingold_tilford(mode="in", root=[0])
g.vs['size'] = ['60']
g.vs['color'] = get_color_arr(N, 3)
g.vs['label'] = ['[ ]', '[a]', '[b]', '[c]', '[ad]', '[ae]',
                 '[af]', '[bd]', '[be]', '[bf]', '[cd]', '[ce]', '[cf]']
g.vs['label_size'] = ['20']

g.write_svg('001.svg', layout=layout, vertex_size=20)
ig.plot(g, layout=layout, bbox=(800, 300), margin=50)
