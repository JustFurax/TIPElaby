# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:03:00 2023

@author: brard

"""

import random
import matplotlib.pyplot as plt
from math import inf



print("la commande fusion(taillex, tailley) genère un labyrinthe")

def vision(labyrinth):
    """
    La focntion vision permet d'afficher avec matplotlib le labyrinthe
    """
    fig, ax = plt.subplots()
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == 1:
                ax.fill([j, j+1, j+1, j], [len(labyrinth)-i, len(labyrinth)-i, len(labyrinth)-i-1, len(labyrinth)-i-1], 'k')
    ax.set_xlim(0, len(labyrinth[0]))
    ax.set_ylim(0, len(labyrinth))
    ax.set_aspect('equal')
    plt.show()


#plot_labyrinth(labyrinth)





def matricemur(largeur, hauteur):
    """
    
    Parameters
    ----------
    largeur : Entier
        longueur du labyrinthe sur x.
    hauteur : Enter
        hauteur dy labyrinthe sur y.

    Returns
    -------
    matrice_dupliquee : liste de liste
        Une matrice qui représente un quadrillage parfait afin de faire la fusion

   
    """
    
    matrice=[]
    sousmatrice=[1,0]*(largeur)
    
    sousmatrice.append(1)
    
    
    matrice1=[1]*(largeur*2)
   
    matrice1.append(1)
    
    for p in range(hauteur):
        
        matrice.append(matrice1)
        matrice.append(sousmatrice)
        
    matrice.append(matrice1)
    
    
    matrice_dupliquee = []
    for ligne in matrice:
        ligne_dupliquee = []
        for caractere in ligne:
            ligne_dupliquee.append(caractere)
        matrice_dupliquee.append(ligne_dupliquee)

    return matrice_dupliquee

    
    
            
def matcoefinitialisation(largeur, hauteur):
    """
    Parameters
    ----------
    largeur : Entier
        taille x du labyrinthe
    hauteur : Entier
        taille y du labyrinthe

    Returns
    -------
    matrice_dupliquee : liste de liste
        Donne la matrice des coefficient au debut de la fusion. Chaque case du labyrinthe a un coefficient different
    """
    
    matrice=[]
    l=1
    
    for p in range(hauteur):
        
        sousmatrice=[]
        
        for n in range (largeur):
        
            sousmatrice.append(l)
            l=l+1
        matrice.append(sousmatrice)
        
    matrice_dupliquee = []
    for ligne in matrice:
        ligne_dupliquee = []
        for caractere in ligne:
            ligne_dupliquee.append(caractere)
        matrice_dupliquee.append(ligne_dupliquee)
    
    return matrice_dupliquee 


def coef(x,y,matcoef): 
    ligne=matcoef[x]
    coef=ligne[y]

    return coef


def selection(matcoef, matmur):
    """
    Parameters
    ----------
    matcoef : Liste de liste
        Matrice des coefficients qui petmet de connaitre les coefficients a chauqes case
    matmur : Liste de liste
        Matrice des murs qui permet de connaitre quelle case a du vide et quelle case a un mur

    Returns
    -------
    matmur : Liste de liste
        Donne la matrice des murs une fois la construction du labyrinthe finie (il est fini quand la matrice des coefficient à le même coefficient a chaque cases)

    """
    #Créer une copie de matcoef
    matcoef_copy = [row[:] for row in matcoef]
    
    xmax = len(matcoef_copy)
    ymax = len(matcoef_copy[0])
    
    x = random.randint(0, xmax - 1)
    y = random.randint(0, ymax - 1)

    sens = random.choice(['horizontal', 'vertical'])
    direction = random.choice(['positif', 'negatif'])

    cell1 = (x, y)
    

    if sens == 'horizontal' and direction == 'positif':
        cell2 = (x + 1, y)
    elif sens == 'horizontal' and direction == 'negatif':
        cell2 = (x - 1, y)
    elif sens == 'vertical' and direction == 'positif':
        cell2 = (x, y + 1)
    elif sens == 'vertical' and direction == 'negatif':
        cell2 = (x, y - 1)

    a, b = cell2

    #print("coos matcoef :", cell1, cell2)

    if a < 0 or b < 0 or a >= xmax or b >= ymax:
        return selection(matcoef_copy, matmur)
    elif matriceunique(matcoef_copy)==True:
        return matcoef_copy, matmur
    elif matcoef_copy[a][b] == matcoef_copy[x][y]:
        return selection(matcoef_copy, matmur)
                    
    check=matcoef_copy[x][y]
    
    for n in range(xmax):
        for p in range(ymax):
            
            if matcoef_copy[n][p] == check:
                
                matcoef_copy[n][p] = matcoef_copy[a][b]

    xmatmur = int(((a * 2 + 1) + (x * 2 + 1)) // 2)
    ymatmur = int(((y * 2 + 1) + (b * 2 + 1)) // 2)

    matmur[xmatmur][ymatmur]=0
    #vision(matmur)
    
    #print(matcoef_copy)
    #vision(matmur)
    #print("recall")
    return selection(matcoef_copy, matmur)
    

def count_number(matrice, nombre):
    """
    Permet de compter le nombre de fois que "nombre" apparait dans une matrice. Cela nous permet d'arreter la fusion quand la construction du labyrinthe est fini
    """
    count = 0
    for row in matrice:
        for element in row:
            if element == nombre:
                count += 1
    return count  


def fusion(x,y):
    """
    

    Parameters
    ----------
    x : Entier
        Taille x.
    y : Entier
        Taille y.

    Returns
    matmur : Liste de liste
        Donne la matrice des murs une fois la construction du labyrinthe finie 
    ----------
    Cette fonction appel les autre fonction pour faire chaques etapes dans l'ordre
    """
    
    matcoef=matcoefinitialisation(x, y)
    matmur=matricemur(x, y)
    vision(matmur)
    matcoef_copy, matmur=selection(matcoef, matmur)
    
    return(matmur)
    
    
    
def matriceunique(matrice):
    """
    Parameters
    ----------
    matrice : Liste de liste
        Matrice.

    Returns
    -------
    bool
        Retourne True si les valeurs des coefficients de la matrice sont toujours les mêmes dans la matrice, False sinon.
    """
    comparateur=matrice[0][0]
    
    for n in range(len(matrice)):
        for p in range(len(matrice[0])):
            
            if comparateur!=matrice[n][p]:
                return False
    return True

def detectimpasse(mat,x,y):
    """
    Teste à des coordonnées x,y si on est dans un configuration impasse c'est à dire que 3 des 4 cases autour sont des murs
    """
    liste=[mat[x][y-1], mat[x+1][y], mat[x][y+1], mat[x-1][y]]
    compteur=0
    
    for n in range(4):
                
        if liste[n]==1:
            compteur+=1
    
    if compteur>=3:
        return True
    else:
        return False
    
def murflottants(matmur, nb):
    """
    Permet d'ajouter un nombre de murs flottants 'nb' en verifiant que l'on retire un mur qui n'est pas dans un angle
    """    
    if nb==0:
        return matmur
    
    xmax = len(matmur)
    ymax = len(matmur[0])
    
    x = random.randint(1, xmax - 2)
    y = random.randint(1, ymax - 2)
    
    if (matmur[x][y]==1 and (matmur[x+1][y]==1 and matmur[x-1][y]==1 or matmur[x][y+1] and matmur[x][y-1]==1)) and detectimpasse(matmur, x,y)==False:

        matmur[x][y]=0
           
        #print(x,y)
    
        return murflottants(matmur, nb-1)
    else:
        return murflottants(matmur, nb)


