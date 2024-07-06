# TIPElaby
TIPELaby est un projet de fin de prépa portant sur l'étude des labyrinthes. Sous licence creactive commons vous pouvez le réutiliser en créditant : Brard Louison et Grichine Nicolas.
<p align="center">
  <img src="https://github.com/JustFurax/TIPElaby/assets/32780530/d283a8c8-ef18-475a-94e7-0b3a704bb576" alt="Description de l'image">
</p>

Nous avons étudiés :
    <ul>
        <li>1 methode de génération (fusion)</li>
        <li>4 methodes de résolution (aleatoire, pompier, flood-fill, Qlearning)</li>
    </ul>
Le but tu TIPE etait de de mesurer le temps de génération et de résolution en fonction des differentes methodes de résolution et de la taille des labyrinthe. Vous trouverez donc dans les codes ce qu'il faut pour mesurer ces parametres.<br />

Vous trouverez aussi dans chaque programme la fonction vision qui permet l'affichage du labyrinthe.<br />

Aussi nous avons introduit le concept de murs flottants et de taille de labytinthe :
<p align="center">
  <img src="https://github.com/JustFurax/TIPElaby/assets/32780530/5950dcde-15ad-461f-b99f-7bf6d83ceb86" alt="Représentaion de la taille et des murs flottants">
</p>

Par convention nos labyrhinte sont stockés dans une variable sous forme de matrices avec un 1 pour un mur et un 0 pour le vide :
<p align="center">
  <img src="https://github.com/JustFurax/TIPElaby/assets/32780530/1e9eebb4-f778-443e-a010-c64699c92ed0" alt="Représentation par matrice">
</p>





<h2>La Generation par fusion (TSI_GEN_FUSION.py)</h2>

La fonction fusion(taillex, tailley) genère un labyrinthe de taille (taillex*2)+1 sur x, (tailley*2)+1 sur y. Car la methode de génération par fusion doit partir d'un labyrinthe de taille impair.<br />
La fonction murflottants(matmur, nb) prend un labyrinthe et ajoute un nombre nb de murs flottants.


