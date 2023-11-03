# On commence par afficher, ou imprimer à la console
# La fonction utilisée est print()
# Exemple: afficher "Hello World !"
print("Hello World!")

# Exemple: afficher "Adama Dian Diallo"
print("Adama Dian Diallo")

# Donc pour afficher un message, il suffit de passer le message à print()

# ------------------------------------------------------------
# Les variables
# Les variables servent à contenir des données en mémoire pour les réutiliser
# Exemple, afficher le nom complet "Adama Dian Diallo"
fullname = "Adama Dian Diallo"
print(fullname)

# Même exemple avec un message plus significatif
fullname = "Adama Dian Diallo"
print("Je m'appelle", fullname)

# Rajoutons une autre variable
fullname = "Adama Dian Diallo"
age = 18
print("Je m'appelle", fullname)
print("J'ai", age, "ans")

# Voilà, c'est très sympa non ?
# Allons plus en profondeur et découvrons les conditions
# Dire si "Adama Dian Diallo" est majeure ou mineure
fullname = "Adama Dian Diallo"
age = 18
print("Je m'appelle", fullname)
print("J'ai", age, "ans")

if age < 18:
    print("Je suis mineure")
else:
    print("Je suis majeure")

# Hourrray !
# Encore, rajoutons une autre variable taille et affichons-la avec un message significatif
fullname = "Adama Dian Diallo"
age = 18
taille = 1.5
print("Je m'appelle", fullname)
print("J'ai", age, "ans")
print("Je mesure", taille, "m")

# Hummm bravo !
# Utilisons encore les conditons pour dire si "Adama Dian Diallo" a les accès pour la foire
# Si elle a plus de 18 ans et mesure plus de 1.2m alors elle a accès, dans le cas contraire, l'accès est refusé
fullname = "Adama Dian Diallo"
age = 12
taille = 1.70

print("Je m'appelle", fullname)
print("J'ai", age, "ans")
print("Je mesure", taille, "m")

if age >= 18 and taille >= 1.2:
    print("Accès autorisé")
else:
    print("Accès refusé")

# Maintenant on va voir comment rendre le programme intéractif en demandant à l'utilisateur des informations
# Très simple il suffit d'utiliser la fonction input()
# Exemple: Lui demander le nom et l'afficher
fullname = input("Votre nom: ")
print("Je m'appelle", fullname)

# Mais attention, si on veut un entier ou un nombre à virgule, il faut les convertir !
# Pour convertir en entier on utilise la fonction int()
# Exemple: lui demander l'age et l'afficher
age = int(input("Votre age: "))
print("J'ai", age, "ans")

# Pour convertir en réel on utilise la fonction float()
# Exemple: lui demander la taille et l'afficher
taille = int(input("Votre taille: "))
print("Je mesure", taille, "m")

# Maintenant, reprenons le programme précedent qui parlait de l'autorisation et rendons-le interactif
fullname = input("Votre nom: ")
age = int(input("Votre age: "))
taille = float(input("Votre taille: "))

print("Je m'appelle", fullname)
print("J'ai", age, "ans")
print("Je mesure", taille, "m")

if age >= 18 and taille >= 1.2:
    print("Accès autorisé")

else:
    print("Accès refusé")