
import numpy as np


# Crea un array 1D con 12 elementi equidistanti tra 0 e 1
equidistante = np.linspace(0, 1, 12)
print("\nArray di 12 numeri equidistanti tra 0 e 1:")
print(equidistante)

# Trasformalo in una matrice 3x4
trasposta3x4 = equidistante.reshape((3, 4))
print("\nMatrice 3x4:")
print(trasposta3x4)

#Genera matrice 3x4 con valori casuali
matricerandom = np.random.rand(3,4)
print("\nMatrice random 3x4 con vaolri 0 e 1: ")
print(matricerandom)

#Somma degli elementi delle matrici

somma_prima = np.sum(equidistante)
somma_seconda = np.sum(matricerandom)
print(f"\nSomma matrice equidistante: {somma_prima}")
print(f"Somma matrice random: {somma_seconda}")