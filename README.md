# Introcution à la programmation python
Nous apprenons les bases de la programmation avec pythons avec quelques notions essentielles
Ce que ce didactitiel couvre:

* [Bases (print, input, conditions)](README.md)
* [Equations affines (conditions)](eq_affine.md)
* [Boucles](boucles.md)
* [Dessins (fonctions, boucles)](dessins.md)

## Les bases
On commence par afficher, ou imprimer à la console

La fonction utilisée est `print()`

**Exemple:** afficher "Hello World !"
```py
print("Hello World!")
```

**Exemple:** afficher `"Adama Dian Diallo"`
```py
print("Adama Dian Diallo")
```

Donc pour afficher un *message*, il suffit de passer le message à `print()`

------------------------------------------------------------
## Les variables
Les variables servent à contenir des données en mémoire pour les réutiliser

**Exemple:** , afficher le nom complet `"Adama Dian Diallo"`
```py
fullname = "Adama Dian Diallo"
print(fullname)
```

Même **exemple** avec un message plus significatif

```py
fullname = "Adama Dian Diallo"
print("Je m'appelle", fullname)
```

Rajoutons une autre variable
```py
fullname = "Adama Dian Diallo"
age = 18
print("Je m'appelle", fullname)
print("J'ai", age, "ans")
```

Voilà, c'est très sympa non ?

Allons plus en profondeur et découvrons les conditions

**Exemple:** Dire si "Adama Dian Diallo" est majeure ou mineure

```py
fullname = "Adama Dian Diallo"
age = 18
print("Je m'appelle", fullname)
print("J'ai", age, "ans")

if age < 18:
    print("Je suis mineure")
else:
    print("Je suis majeure")
```

**Hourrray !**

Encore, rajoutons une autre variable `taille` et affichons-la avec un message significatif

```py
fullname = "Adama Dian Diallo"
age = 18
taille = 1.5
print("Je m'appelle", fullname)
print("J'ai", age, "ans")
print("Je mesure", taille, "m")
```

## Les conditions
Hummm bravo !

Utilisons encore les conditons pour dire si `"Adama Dian Diallo"` a les accès pour la foire

> Si elle a plus de 18 ans et mesure plus de 1.2m alors elle a accès, dans le cas contraire, l'accès est refusé

```py
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
```

Maintenant on va voir comment rendre le programme **intéractif** en demandant à l'utilisateur des informations

Très simple il suffit d'utiliser la fonction `input()`

**Exemple:** Lui demander le nom et l'afficher

```py
fullname = input("Votre nom: ")
print("Je m'appelle", fullname)
```

Mais attention, si on veut un entier ou un nombre à virgule, il faut les convertir !

Pour convertir en entier on utilise la fonction `int()`

**Exemple:** lui demander l'age et l'afficher

```py
age = int(input("Votre age: "))
print("J'ai", age, "ans")
```

Pour convertir en réel on utilise la fonction `float()`

**Exemple:** lui demander la taille et l'afficher

```py
taille = int(input("Votre taille: "))
print("Je mesure", taille, "m")
```

Maintenant, reprenons le programme précedent qui parlait de l'autorisation et rendons-le interactif

```py
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
```

Ensuite, nous allons apprendre les boucles et les fonctions

* [Equations affines](eq_affine.md)
* [Boucles](boucles.md)
* [Dessins (+fonctions, +boucles)](dessins.md)