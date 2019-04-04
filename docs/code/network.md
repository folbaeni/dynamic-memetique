# Code relatif au network

```python
def generation_reseau(numero_gens):
    '''int -> NETWORK
    Ceci crée un network avec seuls les nodes 1 pro capite
    '''
    NETWORK = nx.Graph()
    NETWORK.add_nodes_from(range(1,numero_gens+1))
    return (NETWORK)

def probabilite_numero_amis(network_name):
    ''' str -> int
    Donné le network il calcule aleatoirement selon une probabilité diminuante le numero des amis de x personne
    '''
    gens= len(network_name.nodes.data())
    x = np.random.randint(1,gens,size=10)
    return np.min(x)

def numero_amis(network_name, personne):
    ''' str*int->int
    personne est int parce que on associe des numero aux gens
    donné le network et une personne, il calcule combien des amis il a
    '''
    r=0
    for e,_ in network_name.edges.items():
        f,_=e
        if f==personne:
            r+=1
    return r

def edges_newnetwork(network_name):
    ''' str -> void
    H: Network noveaux
    donné un nouveaux network il crée les edges (liaisons) entre les nodes par rapport à la probabilite des amis
    '''
    gens= len(network_name.nodes.data())
    boucle_temp= copy.deepcopy(network_name.nodes.data())
    for (i,_) in boucle_temp:
        x = probabilite_numero_amis(network_name) - numero_amis(network_name,i)
        if x>0:
            for _ in range(x):
                k= np.random.randint(100)/100
                network_name.add_edge(i,np.random.randint(gens), weight=k)
return()
```
