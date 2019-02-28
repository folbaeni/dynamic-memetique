import basic_network as bn
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#INSERTION PARAMETRES INITIALES
grandeur_network = 50

#FONCTIONS APPELLES
NETWORK = bn.generation_reseau(grandeur_network)
bn.edges_newnetwork(NETWORK)

#DESSIN GRAPHE
nx.draw(NETWORK, with_labels=True)
plt.draw()
plt.show()
