# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:37:44 2024

@author: nicol
"""

# -*- coding: utf-8 -*-



#@author: nicol



import time 
import matplotlib.pyplot as plt

def vision(labyrinth,xu,yu):
    coos=(xu,yu)
    fig, ax = plt.subplots()
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[i])):
            if labyrinth[i][j] == 1:
                ax.fill([j, j+1, j+1, j], [len(labyrinth)-i, len(labyrinth)-i, len(labyrinth)-i-1, len(labyrinth)-i-1], 'k')
    ax.set_xlim(0, len(labyrinth[0]))
    ax.set_ylim(0, len(labyrinth))
    ax.set_aspect('equal')
    x,y=coos
    pltx=x+0.5
    plty=len(labyrinth)-y-0.5
    ax.add_patch(plt.Circle((pltx,plty), radius=0.3, color='r'))
    plt.show()

#faire vision du système a l'arrivée 
  

grid = [[1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,1,1,0,1,0,1],
        [1,0,0,0,1,2,1],
        [1,1,1,1,1,1,1]]

grid2 = [[1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,0,2,1],
         [1,1,1,1,1,1,1,1,1]]

grid3 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

grid4 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
  [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
  [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0, 0, 2, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def pompier(grid):
    it=0
    ligne=1
    colone = 1
    temps = float(0)
  
    direction = 'droite'
    while grid[ligne][colone] != 2:
        
        if direction == 'droite':
            if grid[ligne][colone+1] == 0 and grid[ligne+1][colone+1]==1:
                colone =colone+ 1
                
                it+=1
                
                vision(grid,colone, ligne)
                print(ligne,colone,direction)
                time.sleep(temps)
            elif grid[ligne][colone+1]==0 and grid[ligne+1][colone+1]==0:
                colone =colone + 1
                ligne=ligne+ 1
                
                it+=2
                
                direction = 'bas'
                vision(grid,colone, ligne)
                print(ligne,colone,direction)
                time.sleep(temps)
            elif grid[ligne][colone+1]==2:
                colone = colone +1
            else : 
                direction = 'haut'
        if direction == 'haut':
            if grid[ligne-1][colone]==0 and grid [ligne-1][colone+1] == 1:                
                ligne = ligne -1 
                
                it+=1
                
                vision(grid,colone, ligne)
                print(ligne,colone,direction)
                time.sleep(temps)
            elif grid[ligne-1][colone]==0 and grid [ligne-1][colone+1] == 0:
                colone = colone +1 
                ligne = ligne -1
                
                it+=2
                
                vision(grid,colone, ligne)
                print(ligne,colone,direction)
                time.sleep(temps)
                direction = 'droite'
            elif grid[ligne-1][colone]==2:
                ligne = ligne -1
            else :
                direction = 'gauche'
        if direction == 'gauche':
            if grid[ligne][colone-1] == 0 and grid [ligne-1][colone-1] == 1:              
                colone = colone -1
                
                it+=1
                
                vision(grid,colone, ligne)
                print(ligne,colone,direction)
                time.sleep(temps)
            elif grid[ligne][colone-1] == 0 and grid [ligne-1][colone-1] == 0:
                ligne = ligne -1
                colone = colone -1
                
                it+=2
                
                direction = 'haut'
                print(ligne,colone,direction)
                vision(grid,colone, ligne)
                time.sleep(temps)
            elif grid[ligne][colone-1]==2:
                colone = colone -1                
            else :
                direction = 'bas'
        if direction == 'bas':
            if grid[ligne+1][colone] ==0  and grid [ligne+1][colone-1] ==1:
                ligne = ligne+ 1
                
                it+=1
                
                print(ligne,colone,direction)
                vision(grid,colone, ligne)
                time.sleep(temps)
            elif grid[ligne+1][colone] ==0  and grid [ligne+1][colone-1] ==0:
                colone = colone -1
                ligne = ligne +1
                
                it+=2
                
                direction = 'gauche'
                print(ligne,colone,direction)
                vision(grid,colone, ligne)
                time.sleep(temps)
            elif grid[ligne+1][colone]==2:
                 ligne = ligne +1
                 
                 it+=1
  
            else:
                direction = 'droite'
    return it
                
            
            
            
            
            
    
    
    
    
    
    

    

     

    