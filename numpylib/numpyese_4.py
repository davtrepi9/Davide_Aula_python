"""Consegna:

Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
Somma i due array elemento per elemento per ottenere un nuovo array.
Calcola la somma totale degli elementi del nuovo array.
Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
"""

import numpy as np


# Crea un array 1D con 50 elementi equidistanti tra 0 e 10
equidistante = np.linspace(0, 10, 50)
print("\nArray di 50 numeri equidistanti tra 0 e 10:")
print(equidistante)

#Genera matrice 1D con 50 valori casuali tra 0 e 1
matricerandom = np.random.random(50)
print("\nMatrice random 3x4 con vaolri 0 e 1: ")
print(matricerandom)

#Somma degli elementi delle matrici

nuovamatrice = equidistante+matricerandom
print("\nNuova matrice somma degli elementi delle matrici precedenti: ")
print(nuovamatrice)

# Calcola la somma degli elementi del nuovo array maggiori di 5
somma = np.sum(nuovamatrice[nuovamatrice >5])
print(f"\nSomma dei valori maggiori di 5: {somma}")

