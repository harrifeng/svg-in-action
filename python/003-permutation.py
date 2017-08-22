import igraph as ig
from util import get_color_arr

N = 40
g = ig.Graph.Tree(N, 3)
layout = g.layout_reingold_tilford(mode="in", root=[0])
g.vs['size'] = ['50']
g.vs['color'] = get_color_arr(N, 3)

del_nodes = []

g.vs['label'] = ['[1, 2, 3]',
                 '[1, 2, 3]', '[2, 1, 3]', '[3, 2, 1]',
                 '[1, 2, 3]', '[1, 3, 2]', '[]',
                 '[2, 1, 3]', '[2, 3, 1]', '[]',
                 '[3, 2, 1]', '[3, 1, 2]', '[]']
g.vs['label'] = [''] * N
g.vs[0]['label'] = '123'
g.vs[1]['label'] = '123'
g.vs[2]['label'] = '213'
g.vs[3]['label'] = '321'
g.vs[5]['label'] = '123'
g.vs[6]['label'] = '132'
g.vs[8]['label'] = '213'
g.vs[9]['label'] = '231'
g.vs[11]['label'] = '321'
g.vs[12]['label'] = '312'

g.vs[18]['label'] = '123'
g.vs[21]['label'] = '132'
g.vs[27]['label'] = '213'
g.vs[30]['label'] = '231'
g.vs[36]['label'] = '321'
g.vs[39]['label'] = '312'

g.vs['label_size'] = ['20']

g.delete_vertices(del_nodes)

g.write_svg('003.svg', layout=layout, vertex_size=20)
ig.plot(g, layout=layout, bbox=(1400, 600), margin=50)
