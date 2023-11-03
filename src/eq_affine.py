# Dans ce programme, nous allons penser à comment faire pour résoudre une équation
# affine de la forme ax + b = 0 et d'afficher la solution
# x = -b/a
a = float(input("a: "))
b = float(input("b: "))

if a == 0:
    print("a doit être non nul !")
else :
    x = - b / a
    print("La solution est:", x)