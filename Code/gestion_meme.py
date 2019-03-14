import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import copy

def init_meme(network_name):
    '''NETWORK -> Void
    Il insert un mémé appelé meme comme attribute à un node random et retourne le node 'victime'
    '''
    gens= len(network_name.nodes.data())
    x = np.random.randint(1,gens)
    nx.set_node_attributes(network_name, 0, 'meme')
    network_name.nodes[x]['meme'] = 1
    lm = network_name.edges(x)
    return(x)

def propagation_meme_gen(network_name):
    '''NETWORK -> Void
    propague le meme d'une generation selon le "weight" des edges
    '''
    pres_mem= nx.get_node_attributes(network_name, 'meme')
    i=0
    L_prev=[]
    while i< nx.number_of_nodes(network_name):
        if pres_mem[i]==1:
            L_prev.append(i)
            for (a,b) in network_name.edges(i):
                x = np.random.randint(0,100,size=3)/100
                t=100
                for j in x:
                    if j < t:
                        t=j
                if t >= network_name.get_edge_data(a,b)['weight']:
                    network_name.nodes[b]['meme'] = 1
        i+=1
    for i in L_prev:
        network_name.nodes[i]['meme'] = 0
    return()
