import igraph as ig
g = ig.Graph.Tree(31, 2)
print g
# g.delete_vertices(6)
layout = g.layout_reingold_tilford(mode="in", root=[0])
g.vs['size'] = ['60']


g.vs['color'] = ['#d9534f',
                 '#5cb85c', '#5cb85c',
                 '#428bca', '#428bca', '#428bca', '#428bca'
                 ]

g.vs['label'] = ['0'] * 31
g.vs['label_size'] = ['20']

g.write_svg('002.svg', layout=layout, vertex_size=20)
ig.plot(g, layout=layout, bbox=(800, 300), margin=50)
