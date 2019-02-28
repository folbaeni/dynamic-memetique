import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy

def generation_reseau(numero_gens):
    NETWORK = nx.Graph()
    NETWORK.add_nodes_from(range(1,numero_gens+1))
    return(NETWORK)

def probabilite_numero_amis(network_name):
    gens= len(network_name.nodes.data())
    x = np.random.randint(gens)
    return x

def edges_newnetwork(network_name):
    #Il faut ajouter la probabilité de numero amis
    gens= len(network_name.nodes.data())
    boucle_temp= copy.deepcopy(network_name.nodes.data())
    for (i,_) in boucle_temp:
        x = probabilite_numero_amis(network_name) # - numero amis qu'il a
        for j in range(x):
            network_name.add_edge(i,np.random.randint(gens))
    return()


NETWORK = generation_reseau(10)
edges_newnetwork(NETWORK)


# numphy.random.choice
#random randint

nx.draw(NETWORK, with_labels=True)
plt.draw()
plt.show()