# les boucles
# Permettent de faire des actions répétitives

# Exemple 1:  afficher "Adama" 5 fois, old way
print("Adama")
print("Adama")
print("Adama")
print("Adama")
print("Adama")

# Si on veut plus de "Adama" On fait du copier-coller
# Exemple 2: Afficher "Adama" 10x
print("Adama")
print("Adama")
print("Adama")
print("Adama")
print("Adama")
print("Adama")
print("Adama")
print("Adama")
print("Adama")
print("Adama")

# Maintenant voyons si je veux changer le nom
# je suis obligé de le modifier partout
# Exemple 3 : afficher "Moustapha" 5x
print("Moustapha")
print("Moustapha")
print("Moustapha")
print("Moustapha")
print("Moustapha")

# --------------------------------------------------------------
# Voilà, avec les boucles, on peut faire ça très facilement
# Exemple 4: Afficher "Adama" 5 fois
for i in range(5):
    print("Adama")

# Exemple 5: Afficher "Adama" 10 fois
for i in range(10):
    print("Adama")

# Exemple 6: Afficher "Moustapha" 10 fois
for i in range(10):
    print("Moustapha")

# On peut aussi compter avec les boucles, et même faire des calculs
# Exemple 7 : Afficher de 0 à 9
for i in range(10):
    print(i)

# Exemple 8 : Compter de 1 à 10
for i in range(10):
    print(i + 1)

# Exemple 9 : Calculer la table de multiplication de 10
# 1 x 10 = 10
# 2 x 10 = 20
# 3 x 10 = 30
# ...
# 10 x 10 = 100
valeur = 10
for i in range(10):
    print(i+1, "x", valeur, "=", valeur * (i + 1))

# Voilà, pour une introduction c'est tout !