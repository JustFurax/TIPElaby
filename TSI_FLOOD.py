# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:09:23 2024

@author: nicol
"""
import matplotlib.pyplot as plt
from collections import deque
from math import inf
import random


#------fonctions------------
def maze_vide(x1,y1):
    """
    Parameters
    ----------
    x1 : Entier
        longueur du labyrinthe sur x.
    y1 : Enter
        hauteur dy labyrinthe sur y.

    Returns
    -------
    matrice_dupliquee : liste de liste
        Une matrice vide qui représente le labyrinthe mais juste avec les murs exterieurs.

    """
    
    x,y=x1*2,y1*2
    mat=[]
    matcouvercle=(x+1)*[1]
    matbocal=[1]
    
    for _ in range(y-1):
        matbocal.append(0)
    matbocal.append(1)
    mat.append(matcouvercle)
    
    for n in range(x-1):
        mat.append(matbocal)
        
    mat.append(matcouvercle)
    
    matrice_dupliquee = []
    for ligne in mat:
        ligne_dupliquee = []
        for caractere in ligne:
            ligne_dupliquee.append(caractere)
        matrice_dupliquee.append(ligne_dupliquee)

    return matrice_dupliquee


def direction_min(x,y, matrice):
    """
    Parameters
    ----------
    x : Entier
        Coordonées x de la position actuelle.
    y : Entier
        Coordonées y de la position actuelle.
    matrice : liste de liste
        matrice des distance.

    Returns
    -------
    str
        La direction pour laquelle la matrice des distances donne la valeur minimale en fonction des coordonnées actuelle.

    """
    voisins = []
    
    # Coordonnées relatives des cases voisines
    deplacements = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Nord, Est, Sud, Ouest
    
    # Parcours des déplacements
    for dx, dy in deplacements:
        nx, ny = x + dx, y + dy
        # Vérification si les coordonnées sont valides
        if 0 <= nx < len(matrice) and 0 <= ny < len(matrice[0]):
            voisins.append(matrice[nx][ny])
        else:
            voisins.append(None)
    
    
   
    min_mat=min(voisins)
    
    indices_minimum = [i for i, x in enumerate(voisins) if x == min_mat]
    
    index_aleatoire = random.choice(indices_minimum)

    if index_aleatoire==0:
        return "nord"
    if index_aleatoire==1:
        return "est"
    if index_aleatoire==2:
        return "sud"
    if index_aleatoire==3:
        return "ouest"


def vision(labyrinth, distances, xu,yu, labyrinth2):
    """
 Permet d'afficher avec matplotlib le labyrinthe réel, le labyrinthe découvert, la matrice des distance et les coodonées actuelles
    """
    fig, ax = plt.subplots()
    coos=(xu,yu)
    
    for i in range(len(labyrinth2)):
        for j in range(len(labyrinth2[i])):
            if labyrinth2[i][j] == 1:
                ax.fill([j, j+1, j+1, j], [len(labyrinth2)-i, len(labyrinth2)-i, len(labyrinth2)-i-1, len(labyrinth2)-i-1], 'lightsteelblue')
            if labyrinth2[i][j] == 2:
                ax.fill([j, j+1, j+1, j], [len(labyrinth2)-i, len(labyrinth2)-i, len(labyrinth2)-i-1, len(labyrinth2)-i-1], 'green')
    
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == 1:
                ax.fill([j, j+1, j+1, j], [len(labyrinth)-i, len(labyrinth)-i, len(labyrinth)-i-1, len(labyrinth)-i-1], 'k')
            
            else:
                distance_text = f"{int(distances[i][j])}" if distances[i][j] != inf else "∞"
            
                ax.text(j + 0.5, len(labyrinth)-i - 0.5, distance_text,fontsize=9, ha='center', va='center', color='black')

    ax.set_xlim(0, len(labyrinth[0]))
    ax.set_ylim(0, len(labyrinth))
    ax.set_aspect('equal')
    x,y=coos
    plt.gca().set_axis_off()
    pltx=x+0.5
    plty=len(labyrinth)-y-0.5
    ax.add_patch(plt.Circle((pltx,plty), radius=0.3, color='r'))
    plt.show()
    
    
def matdistances(maze, entree, sortie):
    """
    Parameters
    ----------
    maze : Liste de liste
        Matrice des murs découvert par le robot.
    entree : tuple
        Debut du comptage sur ces coordonnées.
    sortie : tuple
        Comptage jusqu'a ces coordonnées.

    Returns
    -------
    TYPE
        Matrice des distance qui donne les distance entre chaque case et la sortie.


    """
    
    taillex, tailley = len(maze), len(maze[0])
    
    
    queue = deque([(entree[0], entree[1], 0)])
    
    distances = [[float('inf') for i in range(tailley)] for j in range(taillex)]

    while queue:
        x, y, distance = queue.popleft()

        if 0 <= x < taillex and 0 <= y < tailley and maze[x][y] != 1 and distance < distances[x][y]:
            
            distances[x][y] = distance

            if (x, y) == sortie:
                break

            queue.append((x + 1, y, distance + 1))
            queue.append((x - 1, y, distance + 1))
            queue.append((x, y + 1, distance + 1))
            queue.append((x, y - 1, distance + 1))

    return distances



def flood (maze, maze_explore, iteration, min_action):
    """
    Fonction qui appelle les autres fonction pour résoudre le labyrinthe jusqu'a que le labyrinthe soit résolu
    """
    sortie = (len(maze)-2,len(maze)-2)
    length = len(maze[0])
    height = len(maze)
    
    if iteration==0:
        min_action=inf
        iteration=1
        maze_explore = maze_vide ((length//2),(height//2) )
    
    action=0
    ligne = 1
    colone = 1
    
    maze_explore[ligne][colone-1] = maze[ligne][colone-1]

    maze_explore[ligne][colone+1] = maze[ligne][colone+1]

    maze_explore[ligne-1][colone] = maze[ligne-1][colone]

    maze_explore[ligne+1][colone] = maze[ligne+1][colone]
    
    
     # assigne aux labyrinthe en mémoire un labyrinthe vide sans aucun mur, celui ci viendra a être mis a jour au fil de l'éxploration
    #maze_explore = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    while maze[ligne][colone] !=2 :
        action+=1


        
        matrice_de_distances = matdistances(maze_explore,sortie,(ligne,colone))
        
        
        
        direction = direction_min(ligne, colone,matrice_de_distances )
        

        
        
        
        #étape 1 : mouvement de 1 case
        if direction == 'nord':
            ligne = ligne -1
            
        if direction == 'sud':
            ligne = ligne +1
            
            
        if direction == 'est':
            colone = colone +1
            
        if direction== 'ouest':
            colone = colone -1 
            
        maze_explore[ligne][colone-1] = maze[ligne][colone-1]

        maze_explore[ligne][colone+1] = maze[ligne][colone+1]

        maze_explore[ligne-1][colone] = maze[ligne-1][colone]

        maze_explore[ligne+1][colone] = maze[ligne+1][colone]
            
        
        vision (maze_explore, matrice_de_distances,colone, ligne, maze)
    
    if action==min_action:
        return min_action,iteration-1
    
    if action <= min_action:
        print(action)
        iteration+=1
        min_action=action
        return flood(maze, maze_explore, iteration, min_action)
    
    


ligne = 1 #depart
colone = 1

maze_real =  [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

maze_real2 =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
 [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
 [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 2, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


maze_real3 =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 1,1 , 0, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
 [1, 1,1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
 [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]









































