import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy

def init_meme(network_name):
    gens= len(network_name.nodes.data())
    x = np.random.randint(1,gens)
    nx.set_node_attributes(network_name, 0, 'meme')
    network_name.nodes[x]['meme'] = 1