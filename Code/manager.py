import basic_network as bn
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import gestion_meme as meme

#INSERTION PARAMETRES INITIALES
grandeur_network = 60

#FONCTIONS APPELLES
NETWORK = bn.generation_reseau(grandeur_network)
bn.edges_newnetwork(NETWORK)



#INTRODUCTION MEME
zero = meme.init_meme(NETWORK)



#DESSIN GRAPHE

elarge=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] >=0.7]
emedium=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] >0.3 and d['weight']<0.7]
esmall=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] <=0.3]

ememe= NETWORK.edges(zero)

pos=nx.spring_layout(NETWORK) # positions for all nodes

# nodes
ouimeme=[a for a in NETWORK.nodes if NETWORK.nodes[a]['meme']==1]
nonmeme=[a for a in NETWORK.nodes if NETWORK.nodes[a]['meme']==0]

nx.draw_networkx_nodes(NETWORK,pos,
                       nodelist=ouimeme,
                       node_color='b',
                       node_size=150,
                   alpha=0.8)

nx.draw_networkx_nodes(NETWORK,pos,
                       nodelist=nonmeme,
                       node_color='r',
                       node_size=150,
                   alpha=0.8)


# edges
nx.draw_networkx_edges(NETWORK,pos,edgelist=elarge,
                    width=1)
nx.draw_networkx_edges(NETWORK,pos,edgelist=emedium,
                    width=1,alpha=0.7,edge_color='r',style='dashed')
nx.draw_networkx_edges(NETWORK,pos,edgelist=esmall,
                    width=1,alpha=0.4,edge_color='g',style='dashed')
nx.draw_networkx_edges(NETWORK,pos,edgelist=ememe,
                    width=4,alpha=0.3,edge_color='b')

# labels
nx.draw_networkx_labels(NETWORK,pos,font_size=8,font_family='sans-serif')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display

