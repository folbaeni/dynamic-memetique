import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn.apionly as sns
import matplotlib.animation
import basic_network as bn
import gestion_meme as meme

# Create Graph
#INSERTION PARAMETRES INITIALES
grandeur_network = 150
numero_generations = 100

#FONCTIONS APPELLES
NETWORK = bn.generation_reseau(grandeur_network)
bn.edges_newnetwork(NETWORK)


#INTRODUCTION MEME
zero = meme.init_meme(NETWORK) #premier node avec le meme

#INTRODUCTION DEGOUT
meme.degout(NETWORK)


# Build plot
fig, ax = plt.subplots()
fig.clear()
global tralala
tralala=0

global pos

def update(num):
    fig.clear()
    ax.clear()
    meme.propagation_meme_gen(NETWORK)
    #DESSIN GRAPHE
    elarge=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] >=0.7]
    emedium=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] >0.3 and d['weight']<0.7]
    esmall=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] <=0.3]
    ememe= NETWORK.edges(zero) #edges initialies liée au zero de la diffusion du meme
    global tralala
    if tralala==0:
        global pos
        pos=nx.fruchterman_reingold_layout(NETWORK) # positions for all nodes
        tralala=1
    # nodes
    ouimeme=[a for a in NETWORK.nodes if NETWORK.nodes[a]['meme']==1] #marque ceux qui ont les memes
    nonmeme=[a for a in NETWORK.nodes if NETWORK.nodes[a]['meme']==0] #marque ceux qui n'ont pas le meme
    nx.draw_networkx_nodes(NETWORK,pos,
                           nodelist=ouimeme,
                           node_color='b',
                           node_size=80,
                       alpha=0.8)
    nx.draw_networkx_nodes(NETWORK,pos,
                           nodelist=nonmeme,
                           node_color='r',
                           node_size=60,
                       alpha=0.8)
    # edges
    nx.draw_networkx_edges(NETWORK,pos,edgelist=elarge,
                        width=0.4, alpha=0.8)
    nx.draw_networkx_edges(NETWORK,pos,edgelist=emedium,
                        width=0.3,alpha=0.6,edge_color='g',style='dashed')
    nx.draw_networkx_edges(NETWORK,pos,edgelist=esmall,
                        width=0.2,alpha=0.4,edge_color='r',style='dashed')
    nx.draw_networkx_edges(NETWORK,pos,edgelist=ememe,
                        width=4,alpha=0.2,edge_color='b')
    plt.axis('off')


ani = matplotlib.animation.FuncAnimation(fig, update, frames=6, interval=500, repeat=True)
plt.show()