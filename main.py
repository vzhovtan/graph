from typing import Union

import graph

g: graph.Graph = graph.Graph(5, undirected=False)
g.insert_edge(0, 1, 1.0)
g.insert_edge(0, 3, 1.0)
g.insert_edge(0, 4, 3.0)
g.insert_edge(1, 2, 2.0)
g.insert_edge(1, 4, 1.0)
g.insert_edge(3, 4, 3.0)
g.insert_edge(4, 2, 3.0)
g.insert_edge(4, 3, 3.0)

for i in g.nodes:
  print(i.get_edge_list())