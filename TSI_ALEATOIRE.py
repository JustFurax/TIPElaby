# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:10:18 2024

@author: brardl
"""

import random
import matplotlib.pyplot as plt

def vision(labyrinth,coos):
    """
    Parameters
    ----------
    labyrinth : liste de liste
        Matrice des murs du labyrinthe.
    coos : tuples
        Coordonées actuelles du robot.

    La focntion vision permet d'afficher avec matplotlib le labyrinthe en affichant les coordonnées actuelles d'un point rouge
    """
    #coos=(xu,yu)
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
"""    
def testplot(laby):
    
    for n in range(len(laby)):
        for p in range(len(laby[0])):
            vision(laby,p,n)
"""
def aleatoire(laby):
    """
    Parameters
    ----------
    largeur : laby
        Matrice des murs qui représente le labyrinthe
    Returns
    -------
    compteur : Entier
        Compte le nombre de mouvements nécessaire à la resolution
    """
       
    arrivee=(((len(laby))-2),(len(laby[1])-2))
    coos=(1,1)
    vision(laby,coos)
    
    compteur=0
    
    moyliste=[]
    
    
    while(coos!=arrivee):
    
        deplallow=[]
        
        
    
        x,y=coos
    
        deplallow.append(laby[x][y-1])
        deplallow.append(laby[x-1][y])
        deplallow.append(laby[x][y+1])
        deplallow.append(laby[x+1][y])
        
        
        #print(deplallow)
    
        indice=random.randint(0, 3)
        while(deplallow[indice]!=0):
            indice=random.randrange(4)
            
        #print(indice)
        
        if indice==0:
            coos=(x,y-1)
        if indice==1:
            coos=(x-1,y)
        if indice==2:
            coos=(x,y+1)
        if indice==3:
            coos=(x+1,y)
        
        compteur+=1
        print("nouvelles coos", arrivee, coos)
        vision(laby,coos)
        
    print("SORTIE TROUVEE", compteur )
        
    vision(laby,arrivee)   
    
    return(compteur)


def moyaleatoire(laby):
    """
    Cette fonction permet de resoudre 10x un même labyrinthe pour lisser les courbes
    """
    
    liste=[]
    
    for _ in range(10):
        liste.append(aleatoire(laby))
    
    somme=sum(liste)
    moyenne=somme/len(liste)
    
    return liste, moyenne
    
    


