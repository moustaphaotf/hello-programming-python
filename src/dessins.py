# Ici on va faire quelques exercices pratiques
# Il s'agit de faire des programmes pour dessiner à la console
# On utilisera les fonctions

# Les fonctions servent à encapsuler des instructions pour les invoquer tous sous le même nom
# Autrement dit, par exemple, si on veut effectuer une tâche qui regroupe plusieurs sous-tâches, 
# on crée une fonction qui va se charger de faire toutes les sous-tâches

# Point sur les fonctions

# Fonction qui dit bonjour
def dire_bonjour():
    print("Bonjour !")

# Exemple d'exécution
dire_bonjour()

# Fonction qui dit bonjour à une personne
def dire_bonjour1(nom):
    print("Bonjour", nom)


# Exemple d'exécution
dire_bonjour1("Adama")

# Voilà, on a utilisé le paramètre pour passer une information utile à la fonction

# --------------------------------------------------------------------------------
# Fonction qui affiche une ligne
# On utilise les boucles pour répéter l'affichage du point
def ligne(longueur):
    for i in range(longueur):
        print("* ", end="")

# Exemple d'exécution
# Affiche une ligne de longueur 7
ligne(7)


# Fonction qui affiche un carré
# On utilise les boucles pour répéter l'affichage d'une ligne en fonction du côté
def carre(cote):
    for i in range(cote):
        ligne(cote)
        print()

# Exemple d'exécution
# Affiche un carré de côté 7
carre(7)

# Voilà, pour une intro !
# Tu peux aussi penser à dessiner un rectangle, ou même un triangle voire un cercle !
# Le fun ^^