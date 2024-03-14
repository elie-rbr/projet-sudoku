"""
Module: sudoku.py Un programme pour manipuler des grilles de sudoku.

Les variables grille_x peuvent vous servir à tester votre programme.
Elles représentent toutes des grilles de Sudoku valides à divers
stades d'avancement: grille_0 est vide, grille_1 semi-remplie et
grille_2 entièrement remplie.
"""


import random as rd



grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1=[
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]

"""
Les deux fonctions ci-dessous sont données à titre d'exemple.  Le
reste est à programmer à la suite de ces fonctions.
"""


def afficher(x):
    """
    Affiche une grille de sudoku g de taille 9x9 sur le terminal.
    """
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1,9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


#afficher(grille_2)


def ligne(x, i):
    """
    Renvoie la ligne i de la grille de sudoku x
    """
    return x[i-1]


#print(ligne(grille_2, 9))


def colonne(x, j):
    """
    Renvoie la colonne j de la grille de sudoku x
    """
    colonne = []
    for i in range(9):
        colonne.append(x[i][j-1])  #récupère l'élément de la colonne j pour chaque ligne
    return colonne


#print(colonne(grille_2, 3))


def région(x, i):
    """
    Renvoie la région k de la grille de sudoku x
    on obtient la région k avec la formule :
    k = 3 ×((i −1)//3) + ((j −1)//3) + 1
    """
    liste = []
    k = ((((i-1) // 3) * 3) + 2, (((i-1) % 3) * 3) + 2)
    for h in range(-1, 2):
        for j in range(-1, 2):
            liste.append(x[(k[0]+h) - 1][(k[1]+j) - 1])
    return liste


#print(région(grille_2, 7))


def unique(x):
    y = x.copy()
    for i in x:
        y.remove(i)
        if i == 0:
            pass
        elif i in y:
            return False
    return True


#print(unique(colonne(grille_1, 5)))


def ajouter(x, i, j, v):
    """
    Ajoute la valeur v aux coordonnées (i,j) de la grille x.
    Si la valeur est fausse, la grille ne change pas.
    """
    x[i-1][j-1] = v


def verifier(x):
    """
    Vérifie que la grille est correctement remplie.
    """
    for i in range(1,10):
        a = ligne(x,i)
        b = colonne(x,i)
        c = région(x,i)
        if 0 in a or 0 in b or 0 in c:
            return False
        elif unique(a) == False:
            return False
        elif unique(b) == False:
            return False
        elif unique(c) == False:
            return False
    return True


#grille_1[0][2] = 1
#print(grille_1)
#print(verifier(grille_2))


def jouer(x):
    """
    Demande à l'utilisateur une valeur et des coordonnées, puis réaffiche la grille avec
    la valeur ajoutée si elle est correcte, et inchangée sinon.
    """
    liste_elem = []
    for i in range(len(x)):
            for j in x[i]:
                if j != 0:
                    liste_elem.append(j)
    while len(liste_elem) < 81:
        valeur = int(input("demander une valeur"))
        abcisse = int(input("demander une ligne"))
        ordonne = int(input("demander une colonne"))
        liste_elem = []
        for i in range(len(x)):
            for j in x[i]:
                if j != 0:
                    liste_elem.append(j)
        ajouter(x, abcisse, ordonne, valeur)
        if x[abcisse-1][ordonne-1] == valeur:
            liste_elem.append(valeur)
        afficher(x) 


#afficher(grille_1)
#jouer(grille_1)


def solution(x):
    """
    La fonction renvoie un dictionnaire contenant les valeurs possibles pour chaque case 
    vide de x.
    Le dictionnaire est de la forme : {'case 1':[solutions], 'case 2': [solutions], ...}
    """
    dictionnaire = {i : [] for i in range(10)}
    for i in range(9): #on parcourt les lignes:
        for j in range(9): #on parcourt chaque élément de la ligne
            if x[i][j] != 0: #il y a déjà une valeur dans la case
                pass #on ne fait rien
            else:                    
                ligne1 = ligne(x,i+1)
                colonne1 = colonne(x,j+1)
                num_région = 3*((i)//3) + ((j)//3) + 1   
                région1 = région(x, num_région)
                l = []         
                for k in range(1,10):
                    if (k not in ligne1 and k not in colonne1 and k not in région1):
                        l.append(k)
                dictionnaire[len(l)].append((i,j,l.copy()))
    return dictionnaire


#print(solution(grille_1))


def resoudre(x):
    dico = solution(x)
    liste = []
    for i in dico.values():
        liste.extend(i)
    if dico[0] != []:
        return False
    elif liste == []:
        return x
    else:
        for j in liste[0][2]:
            ajouter(x, (liste[0][0]+1), (liste[0][1]+1), j)
            test = resoudre(x)
            if test == False:
                ajouter(x, (liste[0][0]+1), (liste[0][1]+1), 0)
            else:
                return x
    return False


def generer():
    grille = [[0 for i in range(10)] for j in range(10)]
    dico = solution(grille)
    liste = []
    for i in dico.values():
        liste.extend(i)
    liste = rd.shuffle(liste)
    if dico[0] != []:
        return False
    elif liste == []:
        return grille
    else:
        for j in liste[0][2]:
            ajouter(grille, (liste[0][0]+1), (liste[0][1]+1), j)
            test = resoudre(grille)
            if test == False:
                ajouter(grille, (liste[0][0]+1), (liste[0][1]+1), 0)
            else:
                return grille
    return False


def nouvelle():
    """
    Crée une nouvelle grille à résoudre
    """
    grille = generer() # génère une grille complète résolue
    for i in range(rd.randint(0, 64)): # boucle qui va laisser entre 81 et 17 cases remplies
        x = rd.randint(0,8) # on sélectionne une ligne
        y = rd.randint(0,8) # on sélectionne une colonne
        grille[x][y] = 0 # on supprime la valeur de la case sélectionnée
    afficher(grille)

