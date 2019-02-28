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
    x = np.random.randint(1,gens,size=10)
    t=gens
    for i in x:
        if i < t:
            t=i
    return t

def numero_amis(network_name, personne):
    r=0
    for e,_ in network_name.edges.items():
        f,g=e
        if f==personne:
            r+=1
    return r


def edges_newnetwork(network_name):
    gens= len(network_name.nodes.data())
    boucle_temp= copy.deepcopy(network_name.nodes.data())
    for (i,_) in boucle_temp:
        x = probabilite_numero_amis(network_name) - numero_amis(network_name,i)
        if x>0:
            for j in range(x):
                network_name.add_edge(i,np.random.randint(gens))
    return()

#INSERTION PARAMETRES INITIALES
grandeur_network = 50

#FONCTIONS APPELLES
NETWORK = generation_reseau(grandeur_network)
edges_newnetwork(NETWORK)

#DESSIN GRAPHE
nx.draw(NETWORK, with_labels=True)
plt.draw()
plt.show()