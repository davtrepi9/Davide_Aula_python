"""Consegna:
Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.

Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate 
come l'inversione delle righe e la sostituzione condizionale degli elementi."""

import numpy as np

matrice = np.random.randint(1, 101, size=(6,6))
print("\nMatrice 6x6 generata : ")
print(matrice)

centrale = matrice[1:5,1:5]
print("\nSotto-matrice centrale : ")
print(centrale)

inversa = matrice[::-1]
print("\nMatrice con righe invertite : ")
print(inversa)

diagonale = np.diag(matrice)
print("\nDiagonale della matrice : ")
print(diagonale)

inversa[inversa % 3 == 0] = -1
print("\nInversa con multipli di 3 cambiati a -1 : ")
print(inversa)


