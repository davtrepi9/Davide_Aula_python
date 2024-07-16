"""Esercizio 2: Manipolazione di Array Multidimensionali

Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.

Estrarre e stampare la seconda colonna della matrice.

Estrarre e stampare la terza riga della matrice.

Calcolare e stampare la somma degli elementi della diagonale principale della matrice.

"""

import numpy as np

# Crea un array NumPy 2D di 20 numeri sequenziali da 1 a 25.
def genera():
    matrice = np.arange(1, 26).reshape(5,5)
    print("Array contenente 20 numeri equidistanti tra 0 e 10:")
    print(matrice)
    return matrice

# Estrarre e stampare la seconda colonna della matrice
def seconda_colo(matrice):
    secondacl = matrice[:,1]
    print("Seconda colonna della matrice:")
    print(secondacl)
    return secondacl

# Estrarre e stampare la terza riga della matrice
def terza_riga(matrice):
    terza_ri = matrice[2, :]
    print("Terza riga della matrice:")
    print(terza_ri)
    return terza_ri

#Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
def somma_diago(matrice):
    diagonale_somma = np.trace(matrice)
    print("Somma degli elementi della diagonale principale:")
    print(diagonale_somma)
    return diagonale_somma

random_array = None

while True:
    print("\nMenu:")
    print("1. Crea una matrice 5x5")
    print("2. Estrai seconda colonna")
    print("3. Estrai terza riga")
    print("4. Somma diagonale principale")
    print("5. Esci")

    seleziona = input("Scegli un'opzione: ")
        
    if seleziona.isalpha():
            print("Errore Input ")
            break
    if seleziona.isspace():
            print("Errore Input ")

    if seleziona == '1':
        random_array = genera()
    elif seleziona == '2':
        if random_array is not None:
            seconda_colo(random_array)
        else:
            print("Crea prima l'array!")
    elif seleziona == '3':
        if random_array is not None:
            terza_riga(random_array)
        else:
            print("Crea prima l'array!")
    elif seleziona == '4':
         if random_array is not None:
            somma_diago(random_array)
    elif seleziona == '5':
        break
    else:
        print("Scelta non valida. Riprova.")