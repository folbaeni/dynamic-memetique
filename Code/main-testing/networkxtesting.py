import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.Graph()
G.add_nodes_from(range(1,10))

G.add_edge(1,5)
G.add_edges_from([(3,4),(6,7),(3,5)])


nx.draw(G, with_labels=True)
plt.draw()
plt.show()