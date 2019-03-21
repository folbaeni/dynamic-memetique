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
    nx.set_edge_attributes(network_name, 0, 'meme')
    network_name.nodes[x]['meme'] = 1
    lm = network_name.edges(x)
    return(x)

def degout(network_name):
    gens= len(network_name.nodes.data())
    nx.set_node_attributes(network_name, 0, 'degout')
    for i in range(gens):
        pra = np.random.randint(0,10)/10
        if pra>0.7:
            network_name.nodes[i]['degout'] = 1
    return()

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
                network_name.edges[a,b]['meme']= 0
                if network_name.nodes[b]['degout']==0:
                    x = np.random.randint(0,100,size=20)/100
                    t=100
                    for j in x:
                        if j < t:
                            t=j
                    if t >= network_name.get_edge_data(a,b)['weight']:
                        network_name.nodes[b]['meme'] = 1
                        network_name.edges[a,b]['meme']= 1
        i+=1
    for i in L_prev:
        j = np.random.randint(0,10)/10
        if j>0.5:
            network_name.nodes[i]['meme'] = 0
    return()
