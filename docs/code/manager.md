# Code relatif au fonctionnement du modèle

```python
#des variables
grandeur_network = 200
prob_perte_meme = 0.3

#init network
NETWORK = bn.generation_reseau(grandeur_network)
bn.edges_newnetwork(NETWORK)

#init meme
global zero
zero = meme.init_meme(NETWORK,'meme') #premier node avec le meme
nx.set_node_attributes(NETWORK, 0, 'degout')


# Build plot
fig, ax = plt.subplots()
fig.clear()
global tralala
tralala=0
global pos

def update(num):
    fig.clear()
    ax.clear()
    meme.propagation_meme_gen(NETWORK,'meme',prob_perte_meme)
    elarge=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['weight'] >=0.7]
    global zero
    ememe= NETWORK.edges(zero) #edges initialies liée au zero de la diffusion du meme
    eememe=[(u,v) for (u,v,d) in NETWORK.edges(data=True) if d['meme'] ==1]
    global tralala
    if tralala==0:
        global pos
        pos=nx.fruchterman_reingold_layout(NETWORK) # positions for all nodes
        tralala=1
    # nodes
    ouimeme=[a for a in NETWORK.nodes if NETWORK.nodes[a]['meme']==1] #marque ceux qui ont les memes
    nonmeme=[a for a in NETWORK.nodes if NETWORK.nodes[a]['meme']==0] #marque ceux qui n'ont pas le meme
    if ouimeme==[]:
        zero = meme.init_meme(NETWORK,'meme')
        nx.set_node_attributes(NETWORK, 0, 'degout')
    nx.draw_networkx_nodes(NETWORK,pos,edgecolors='black',nodelist=ouimeme,node_color='b',node_size=100,alpha=0.8)
    nx.draw_networkx_nodes(NETWORK,pos,edgecolors='black',nodelist=nonmeme,node_color='r',node_size=100,alpha=0.8)
    # edges
    nx.draw_networkx_edges(NETWORK,pos,edgelist=eememe,width=2, alpha=0.8,edge_color='r',style='dashed')
    nx.draw_networkx_edges(NETWORK,pos,edgelist=elarge,width=0.2, alpha=0.8)
    nx.draw_networkx_edges(NETWORK,pos,edgelist=ememe,width=3,alpha=0.2,edge_color='b')
    plt.axis('off')

ani = matplotlib.animation.FuncAnimation(fig, update, frames=6, interval=700, repeat=True)

plt.show()
```
