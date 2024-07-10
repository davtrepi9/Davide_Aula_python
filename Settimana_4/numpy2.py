import numpy as np


#ESERCIZIO 1

# Crea un array di 10 elementi, tutti uguali a 5
array_fives = np.full(10, 5)
print("Array di 10 elementi, tutti uguali a 5:")
print(array_fives)

# Cambia la forma dell'array creato in una matrice 2x5
matrix_2x5 = array_fives.reshape((2, 5))
print("\nMatrice 2x5 ottenuta cambiando la forma dell'array:")
print(matrix_2x5)

# Crea un array di numeri casuali tra 0 e 1 di dimensione 4x4
random_matrix_4x4 = np.random.rand(4, 4)
print("\nArray di numeri casuali tra 0 e 1 di dimensione 4x4:")
print(random_matrix_4x4)


print("\n")

#ESERCIZIO2

# Crea due array di dimensione 3x3
array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

array2 = np.array([[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])

# Calcola il loro prodotto elemento per elemento
elementwise_product = array1 * array2
print("Prodotto elemento per elemento dei due array 3x3:")
print(elementwise_product)

# Crea un array 3x3 con valori da 1 a 9
array_3x3 = np.arange(1, 10).reshape((3, 3))

# Calcola la somma di tutti gli elementi dell'array
sum_elements = np.sum(array_3x3)
print("\nSomma di tutti gli elementi dell'array 3x3:")
print(sum_elements)
print("\n")

#ESERCIZIO 3


# Crea un array contenente 20 numeri equidistanti tra 0 e 10
array_equidistant = np.linspace(0, 10, 20)
print("Array contenente 20 numeri equidistanti tra 0 e 10:")
print(array_equidistant)

# Utilizza numpy.random per generare un array di numeri interi casuali tra 1 e 100 di dimensione 5x5
random_integers_5x5 = np.random.randint(1, 101, size=(5, 5))
print("\nArray di numeri interi casuali tra 1 e 100 di dimensione 5x5:")
print(random_integers_5x5)

print("\n")


#ESERCIZIO 4

# Crea un array di numeri casuali di dimensione 5x5
random_array_5x5_1 = np.random.rand(5, 5)

# Calcola la media dei valori di ciascuna colonna
mean_columns = np.mean(random_array_5x5_1, axis=0)
print("Array di numeri casuali di dimensione 5x5:")
print(random_array_5x5_1)
print("\nMedia dei valori di ciascuna colonna:")
print(mean_columns)

# Crea un altro array di numeri casuali di dimensione 5x5
random_array_5x5_2 = np.random.rand(5, 5)

# Calcola la somma dei valori di ciascuna riga
sum_rows = np.sum(random_array_5x5_2, axis=1)
print("\nAltro array di numeri casuali di dimensione 5x5:")
print(random_array_5x5_2)
print("\nSomma dei valori di ciascuna riga:")
print(sum_rows)
print("\n")


#ESERCIZIO 5


# Crea un array 1D con 12 elementi
array_1d = np.arange(12)
print("Array 1D con 12 elementi:")
print(array_1d)

# Trasformalo in una matrice 3x4
matrix_3x4 = array_1d.reshape((3, 4))
print("\nMatrice 3x4:")
print(matrix_3x4)

# Estrai la prima colonna dalla matrice creata
first_column = matrix_3x4[:, 0]
print("\nPrima colonna della matrice:")
print(first_column)

# Sostituisci la prima colonna con un array di zeri
matrix_3x4[:, 0] = np.zeros(3)
print("\nMatrice 3x4 dopo la sostituzione della prima colonna con un array di zeri:")
print(matrix_3x4)


#ESERCIZIO 6


# Utilizza numpy.random per generare un array di numeri interi casuali tra 50 e 100 di dimensione 3x3
random_array_3x3 = np.random.randint(50, 101, size=(3, 3))
print("Array di numeri interi casuali tra 50 e 100 di dimensione 3x3:")
print(random_array_3x3)

# Trova il massimo e il minimo valore di questo array
max_value = np.max(random_array_3x3)
min_value = np.min(random_array_3x3)
print("\nMassimo valore dell'array:")
print(max_value)
print("Minimo valore dell'array:")
print(min_value)

# Crea due array 1D di dimensione 5 con numeri casuali
array_1D_1 = np.random.rand(5)
array_1D_2 = np.random.rand(5)
print("\nPrimo array 1D di dimensione 5 con numeri casuali:")
print(array_1D_1)
print("Secondo array 1D di dimensione 5 con numeri casuali:")
print(array_1D_2)

# Trova il prodotto scalare tra i due array
dot_product = np.dot(array_1D_1, array_1D_2)
print("\nProdotto scalare tra i due array:")
print(dot_product)
print("\n")