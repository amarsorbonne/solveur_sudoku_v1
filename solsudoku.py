grille = [
    [0, 6, 4, 0, 0, 9, 0, 3, 8],
    [5, 0, 0, 7, 3, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [8, 7, 1, 0, 0, 0, 0, 4, 0],
    [3, 0, 9, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 4, 0, 0, 8, 9, 0],
    [0, 2, 0, 0, 6, 8, 0, 0, 0],
    [9, 0, 0, 3, 0, 2, 0, 8, 0],
    [0, 0, 3, 0, 9, 0, 0, 5, 0],
] # Grille Sudoku

# Lignes

def ligne(grille,iligne,icolonne):
    """
    return un tableau des valeurs non nulles de la ligne 
    """
    
    return [valeur for valeur in grille[iligne] if valeur != 0]

def verifieligne(grille,iligne,icolonne):
    """
    vérifie la ligne
    """
    
    s = ligne(grille,iligne)
    return len(s) == len(set(s))

# Colonnes 

def colonne(grille,iligne,icolonne):
    """
    return le tableau de la colonne
    """
    return [grille[ligne][icolonne] for ligne in range(9) if grille[ligne][icolonne] != 0] 


def verifie_colonne(grille,iligne,icolonne): 
    """
    vérifie la colonne
    """
    s = colonne(grille,iligne,icolonne)

    return len(s) == len(set(s)) 

# Sous-Cases 

def souscases(grille,iligne,icolonne):
    """
    return la sous case 
    """
    valeurs = []

    startc = (icolonne//3) * 3
    startl = (iligne//3) * 3

    return [grille[startl + i][startc + j] for i in range(3) for j in range(3) if grille[startl + i][startc + j] != 0]

def verifie_sousgrille(grille, iligne, icolonne): 
    """
    Vérifie si une sous-grille (3x3) dans une grille de Sudoku est valide.
    """
    valeurs = souscases(grille,iligne,icolonne)
    return len(valeurs) == len(set(valeurs))

# Prémisses du Solveur

def possibilites(grille,iligne,icolonne) :
    """
        À partir de la grille de Sudoku, j'aimerai qu'une boucle parcours la ligne de sudoku et propose des possibilités à chaque case, 
        puis dans un tableau avec 9 lignes de 9 colonnes j'aimerai intégré toutes les valeurs vrais possibles de la case

        exemple: possibilite[1][1]=[1,2,3,4,5,6,7,8,9]
        exemple: possibilite[]
    """
    possibilite=[1,2,3,4,5,6,7,8,9]

    tabligne = ligne(grille,iligne,icolonne)
    tabcolonne = colonne(grille,iligne,icolonne)
    tabsouscases = souscases(grille,iligne,icolonne)

    if grille[iligne][icolonne]!=0:
        return []
    else : 
        asupprimer = set(tabligne).union(set(tabcolonne)).union(tabsouscases)
        possibilite = list(set(possibilite) - asupprimer)
    
    return possibilite

def posstoutgrille(grille):
    tab=[]
    for iligne in range(9):
        for icolonne in range(9):
            tab.append(possibilites(grille,iligne,icolonne))
    
    return tab

def appposstoutgrille(grille):
    tab=posstoutgrille(grille)
    updated = False
    for i in range(len(tab)):
        if len(tab[i]) == 1:
            grille[i//9][i%9]=tab[i][0]
            updated = True

    return updated

def grille_complete(grille):
    """
    Vérifie si la grille est complète, c'est-à-dire qu'il n'y a plus de cases vides (0).
    """
    for ligne in grille:
        if 0 in ligne:
            return False
    return True

def solve_grille(grille):
    while not grille_complete(grille):
        updated = appposstoutgrille(grille)

        if not updated:
            print("La grille est bloqué")
            break

    for ligne in grille:
        print(ligne)

solve_grille(grille)