# La diffusion des mèmes parmi les reseaux sociaux

> **Quels critères influencent la visibilité d'un même?**

## Le mème

L’intéresse commun pour la mémétique et les mots de Richard Dawkins ont
formé le binome auteur de ce document. Il se propose de analyser et
comprendre l’interaction des mèmes sur internet et en particulier sur
les réseaux sociaux. Pour arriver à cet objectif nous avons développé
nos dossiers personnels en se rapprochant à l’argument, puis nous avons
parcouru le sujet de la mémétique selon la méthode de l’OLMDP pour en
comprendre l’ensemble et conclure sur la spécificité des réseaux.

//Definition meme

### Recherche bibliographique

* [Documentation sur le mème](doc.md)
* [Les lieux du mème](lieux.md)
* [Métiers et disciplines liées au mème](metiers.md)

blah blab ,ce qui a déjà été fait sur le sujet,Dans quelles conditions,les points forts et faibles des travaux existants

* [Études dans ce champ](dejafait.md)

## Travail preliminaire

// depuis nos études bla bla
Le mème est un objet fascinant dont on semble connaitre le
fonctionnement, bien que celui demeure néanmoins difficile a reproduire
« artificiellement » car imprévisible. Par ailleurs aux vu des enjeux
naissant autour de cet objet, de plus de métiers vont venir éclaircir
ces problématiques dans les années à venir.

### Hypothèses

***Il y a des mèmes qui ont plus de facilité à survivre et à se diffuser.***

* différents réseaux ont des vitesses de diffusion différentes
* un mème réussit est forcement diffuse par la diffusion d'un compte important
* un mème contenant une choix A ou B a plus tendance à être diffusé
* en fonction du pays un reseaux est plus visible que les autres

### Critères d'évaluation

En general, un critere permet d'apprecier le degre d'atteinte des resultats, des objectifs.
Ce sont les repers que l'on choisit pour servir de base à notre jugement. Ils precisent ce que l'on attend, sur quel aspect va porter notre jugement.
La liste des criteres pourrait etre grande, c'est à l'équipe de choisir ce qui est important pour elle, ce qu'elle attend plus precisemment comme prise de conscience, comme responsabilisation, comme amelioration.

Une coherence est indispensable entre les objectifs, les strategies et les criteres d'evaluation.

### Objectif

***Évaluer les critères de réussite d'un mème sur les réseaux sociaux et en modeliser la diffusion dans un environnement restreint.***

## Modelisation

Modeliser l'integrité d'un réseaux sociaux avec tous les variables à tenir en compte est impossible car il demanderait une puissance de calcul en dehors des capacités de la pluspartie des ordinateurs.
Pour cette raison le modèle est constitué d'une façon simplifiée, contient un réseau restraint avec un calcul maximale sur un groupe de 500-700 personnes. Les amitiés sont réciproques, du coup il n'existe pas le concept de "follow": s'il y a une amitié entre A et B, les informations voyagent dans les deux sens.
De plus, chaque liaison est marquée par un poids qui peut varier de 0 à 1 et indique la proximité des deux individus, c'est à dire la probabilité et la fréquence des transitions des mèmes entre eux. Pour ce qui concerne les graphes on a choisir de raprésenter par un trait gris seulement les liaison les plus fortes afin de maintenir la propreté et facilité d'analyse.
Ensuite, un point critique a été le phenomnène de retour du mème à quelqu'un qui l'avait déjà: on a choisi d'avoir une probabilité de perdre le mème une fois qui'il le possède. Cela correspond dans la réalité au fait de perdre intêret das un fait ou arrêter d'utiliser une certaine façon de faire. Une fois que quelqu'un a perdu le meme, il n'aura plus la possibilté de le reprendre dans le cas qu'il le reçoit. Cela s'eloigne de la réalité, mais prendre en compte ce facteur nous obligerait à augmenter à la puissance 10 la quantité de nos calculs.

![Animation modèle](assets/gifs/200_02.gif)

### Code

La partie de code a été divisée en trois grandes problematiques, ce qui correspond après à la subdivision en modules du programme:

* Creation d'un network qui soit manipulable représentable
* Insertion d'un mème dans le network et donner des loi de diffusion
* Assemblage des parties avec une facilité à changer les variables

![Animation modèle](assets/gifs/50_02.gif)
> Rapresentation d'un meme dans un network avec 50 personnes.

Même si on n'a pas utilisé Jupyter Notebook pour coder ni rédiger notre projet, nous avons appuyé le code sur l'environnement Anaconda.
Par conséquent nous avons utilisés les librairies de numpy, matplotlib (en particulièr pyplot et animaton) et seaborn.

#### Network

[Code relatif](code/network.md)

blah blah

#### Meme

[Code relatif](code/ges_meme.md)

blah blah

### Finalisation

[Code relatif](code/manager.md)

blah blah

## Analyse



Tableau statistique:
20 simulations par cellule.


On a caculé la probabilité que le même survive plus de 20 générations

:spades:| 50 | 100 | 200 | 400
--------| ---| ----| ----| ---
0.2 | 10% | 20% | 50% | 65%
0.3 | 5% | 10% | 30% | 45%
0.5 | 0% | 5% | 15% | 30%

On a calculé la probabilité que le même atteigne 70% de diffusion

:hearts:| 50 | 100 | 200 | 400
--------| ---| ----| ----| ---
0.2 | 15% | 25% | 40% | 55%
0.3 | 5% | 15% | 35% | 45%
0.5 | 0% | 5% | 15% | 25%

On a calculé la probabilité qu'un même revienne à son expéditeur

:clubs:| 50 | 100 | 200 | 400
-------| ---| ----| ----| ---
0.2 | 25% | 65% | 90% | 98%
0.3 | 15% | 45% | 75% | 95%
0.5 | 5% | 35% | 65% | 80%

:diamonds:




## Conclusion

blah blah
