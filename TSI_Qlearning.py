# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:46:11 2021

@author: PC
"""

import numpy as np
from random import randint
import random
import time
from math import inf


import matplotlib.pyplot as plt
import time

"""
Actions:  0 à 7
    0 1 2
    3   4
    5 6 7
"""

def vision(labyrinth,coos):
    """
    La focntion vision permet d'afficher avec matplotlib le labyrinthe en affichant les coordonnées actuelles d'un point rouge
    """
    fig, ax = plt.subplots()
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == 1:
                ax.fill([j, j+1, j+1, j], [len(labyrinth)-i, len(labyrinth)-i, len(labyrinth)-i-1, len(labyrinth)-i-1], 'k')
    ax.set_xlim(0, len(labyrinth[0]))
    ax.set_ylim(0, len(labyrinth))
    ax.set_aspect('equal')
    y,x=coos
    pltx=x+0.5
    plty=len(labyrinth)-y-0.5
    ax.add_patch(plt.Circle((pltx,plty), radius=0.3, color='r'))
    plt.show()

def action_possible(mat, x, y):
    """
    La fonction action_possion va desactiver les action qui sont impossibles a cause des murs.
    Elle va donc prendre la matrice des murs et les coordonnes actuelles pour retourner une liste des actions possibles.    
    """

    action = [[0,0],[-1,0],[0,0], [0,-1],[0,1],  [0,0],  [1,0] , [0,0]]
    
    if mat[x][y-1]==1:
        action[1]=[0,0]
    if mat[x-1][y]==1:
        action[3]=[0,0]
    if mat[x+1][y]==1:
        action[4]=[0,0]
    if mat[x][y+1]==1:
        action[6]=[0,0]
    
    return action
        
    

def step(action):
    """
    La fonction step execute le mouvement demandé
    """
    # pour rester dans la zone de jeu
    ys = max(0, min(y + actions[action][0],nb_colonnes-1))
    xs = max(0, min(x + actions[action][1],nb_lignes-1))

    return xs,ys,(ys*nb_lignes+xs+1) , grid[ys][xs]


def is_finished():
    """
    La fonction is_finished fait un return quand le robot arrive sur la case d'arrivée, cela permet de detecter qu'on a fini la resolution
    """
    return grid[y][x]== maxi # maxi=recompense arrivée

def take_action(st, Q, eps):
    """
    La fonction take_action choisi si on fait une action aleatoire ou la mieux selon la Qtable en fonction de eps, puis il execute l'action
    """
    # Action aléatoire
    actions=action_possible(matmur, x, y)
    
    if random.uniform(0, 1) < eps:
        action = randint(0, 7)
    else:           # ou action optimale
        action = np.argmax(Q[st])
        
    return action 


def config_base(matmur, xmax, ymax):
    """
    La fonction config base permet d'etablir les bonus et malus.
    Malus de -5 dans les impasses
    Bonus de +10 à l'arrivée
    
    -88 sur les murs pour la visualisation dans l'IDE
    """
    for y in range(ymax+1):
        
        for x in range(xmax+1):
            
            if detectimpasse(matmur, x+1, y+1)==True: #malus impasses
                
                grid[x+1][y+1]=-5
            
            if matmur[x][y]==1: #detection des murs pour visialisation
                
                grid[x][y]=-88
        
    grid[xmax][ymax]=10 #bonus arrivée
    
    
def detectimpasse(mat,x,y):
    """
    Teste à des coordonnées x,y si on est dans un configuration impasse c'est à dire que 3 des 4 cases autour sont des murs
    """

    if x==len(mat)-1 or y==len(mat[0])-1:
        return False
    
    liste=[mat[x][y-1], mat[x+1][y], mat[x][y+1], mat[x-1][y]]
    compteur=0
            
    for n in range(4):
                
        if liste[n]==1:
            compteur+=1
    
    #print(compteur)
    if compteur>=3:
        return True
    else:
        return False



def init():
    """
    Initialise le Qlearning en se potionnant au depart
    """
                
    # Position de départ
    st = y_start * nb_lignes + x_start +1
    return 1,1,st
    
"""
Actions:  0 à 7
    0 1 2
    3   4
    5 6 7
"""
actions = [[0, 0],[-1, 0],[0, 0], [0, -1],[0, 1],  [0, 0],  [1, 0] , [0, 0]]
                               


# **************************************************************************
matmur=[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

y_start = 1
x_start = 1
nb_lignes,nb_colonnes = len(matmur)-1,len(matmur[1])-1
maxi = 10
                                   # valeur maxi du champ de potentiel

# grille trajet
grid = []
grid += [[0.0]*nb_lignes for i in range(nb_colonnes)]
grid = np.array(grid)

# Etats (état 1 non utilisé)
Q=[]
nb_actions,nb_cases = 8,(nb_lignes * nb_colonnes )+1
Q += [[0.0]*nb_actions for i in range(nb_cases)]
Q = np.array(Q)

config_base(matmur, nb_lignes-1 ,nb_colonnes-1)
x,y,st= init()


mouvementsmin=48 +1 #Correspond au nombre de mouvements minimums nécéssaires afin de résoudre le labyrinthe (calculé avec djikstra ou Flood)
mouvements=inf

i=0
# Mise à jour par renforcement
while mouvements>=mouvementsmin:
    i+=1
    x,y,st = init()
    #print("depart: ",i+1)
    j=0
    x1,y1=1,1
    compteur=0
    liste=[]
    
    while not is_finished():
        
        at = take_action(st, Q, 0.8)
        x,y,stp1, r = step(at)
        
        liste.append((x1,y1))
        
        if (x,y) not in liste:
            compteur+=1
            
        x1,y1=x,y
        
        #Mise à jour de la  Q fonction
        atp1 = take_action(stp1, Q, 0.0)
        Q[st][at] = Q[st][at] + 0.2*(r + 0.9*Q[stp1][atp1] - Q[st][at])

        j=j+1
        st = stp1
        
    mouvements=compteur
    
print("Departs", i)
        
    
# Enregistrement de la trajectoire finale
trajectoire=[]
x,y,st= init()
trajectoire.append((x_start,y_start))
n=0

while not is_finished() and n < 50:
#for i in range(40):
    at = take_action(st, Q, 0.0)
    x,y,stp1, r = step(at)
    trajectoire.append((x,y))
    st = stp1
    n=n+1

for i in range(len(trajectoire)):
    grid[trajectoire[i][1]][trajectoire[i][0]]=88
    
    
grid = np.hstack((grid, np.full((grid.shape[0], 1), -88)))
new_row = np.full((1, grid.shape[1]), -88)
grid = np.vstack((grid, new_row))

#print(grid)

