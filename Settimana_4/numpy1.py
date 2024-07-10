import numpy as np

#ESERCIZIO 1

print("ESERCIZIO 1 \n")
# 1. Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49
array_integers = np.arange(10, 50)

# 2. Verifica il tipo di dato dell'array e stampa il risultato
dtype_integers = array_integers.dtype
print(f"Tipo di dato dell'array (prima conversione): {dtype_integers}")

# 3. Cambia il tipo di dato dell'array in float64
array_floats = array_integers.astype(np.float64)

# Verifica di nuovo il tipo di dato
dtype_floats = array_floats.dtype
print(f"Tipo di dato dell'array (dopo conversione): {dtype_floats}")

# 4. Stampa la forma dell'array
shape_array = array_floats.shape
print(f"Forma dell'array: {shape_array}\n")


#ESERCIZIO 2
print("ESERCIZIO 2\n")
# Creare un array di 12 numeri equidistanti tra 0 e 1 usando linspace
array_linspace = np.linspace(0, 1, 12)

# Cambiare la forma dell'array a una matrice 3x4
matrix_linspace = array_linspace.reshape((3, 4))

# Generare una matrice 3x4 di numeri casuali tra 0 e 1
matrix_random = np.random.rand(3, 4)

# Calcolare la somma degli elementi della matrice linspace
sum_linspace = np.sum(matrix_linspace)

# Calcolare la somma degli elementi della matrice random
sum_random = np.sum(matrix_random)

# Stampare i risultati
print("Matrice linspace 3x4:\n", matrix_linspace)
print("Somma degli elementi della matrice linspace:", sum_linspace)

print("\nMatrice random 3x4:\n", matrix_random)
print("Somma degli elementi della matrice random:", sum_random)
print("\n")

