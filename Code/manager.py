import basic_network as bn
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import gestion_meme as meme
import matplotlib.animation as animation

#INSERTION PARAMETRES INITIALES
grandeur_network = 100
numero_generations = 100

#FONCTIONS APPELLES
NETWORK = bn.generation_reseau(grandeur_network)
bn.edges_newnetwork(NETWORK)



#INTRODUCTION MEME
zero = meme.init_meme(NETWORK) #premier node avec le meme


for i in range(numero_generations):
    meme.propagation_meme_gen(NETWORK)


#DESSIN GRAPHE

elarge=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] >=0.7]
emedium=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] >0.3 and d['weight']<0.7]
esmall=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] <=0.3]

ememe= NETWORK.edges(zero) #edges initialies liée au zero de la diffusion du meme

pos=nx.spring_layout(NETWORK) # positions for all nodes
#    pos=nx.get_node_attributes(NETWORK,'pos')

# nodes
ouimeme=[a for a in NETWORK.nodes if NETWORK.nodes[a]['meme']==1] #marque ceux qui ont les memes
nonmeme=[a for a in NETWORK.nodes if NETWORK.nodes[a]['meme']==0] #marque ceux qui n'ont pas le meme

nx.draw_networkx_nodes(NETWORK,pos,
                       nodelist=ouimeme,
                       node_color='b',
                       node_size=50,
                   alpha=0.8)

nx.draw_networkx_nodes(NETWORK,pos,
                       nodelist=nonmeme,
                       node_color='r',
                       node_size=30,
                   alpha=0.8)


# edges
nx.draw_networkx_edges(NETWORK,pos,edgelist=elarge,
                    width=0.5)
nx.draw_networkx_edges(NETWORK,pos,edgelist=emedium,
                    width=0.4,alpha=0.7,edge_color='g',style='dashed')
nx.draw_networkx_edges(NETWORK,pos,edgelist=esmall,
                    width=0.3,alpha=0.4,edge_color='r',style='dashed')
nx.draw_networkx_edges(NETWORK,pos,edgelist=ememe,
                    width=4,alpha=0.3,edge_color='b')

# labels
    #nx.draw_networkx_labels(NETWORK,pos,font_size=8,font_family='sans-serif')

plt.axis('off')
#name = "graph" + str(i) + ".png"
#plt.savefig(name) # save as png
plt.show() # display

