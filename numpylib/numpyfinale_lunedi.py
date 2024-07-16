"""Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing."""

import numpy as np


# Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
def crea_array1d():
    random_array = np.random.randint(10, 50, size=20)
    print("\nArray di numeri interi casuali compresi tra 10 e 50:")
    print(random_array)
    return random_array

# Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
def slicing_f10(random_array):
    slicing1 = random_array[0:10]
    print("\nPrimi 10 elementi:")
    print(slicing1)
    return slicing1

#Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
def slicing_l5(random_array):
    slicing1 = random_array[15:20]
    print("\nUltimi 5 elementi:")
    print(slicing1)
    return slicing1

#Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
def slicing_5to15(random_array):
    slicing1 = random_array[4:14]
    print("\nDa 5 index al 15 index :")
    print(slicing1)
    return slicing1

#Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
def slicing_3th(random_array):
    slicing1 = random_array[2:19:3]
    print("\nTerzo elemento :")
    print(slicing1)
    return slicing1

#Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
def slicing_99(random_array):
    random_array[4:9] = 99
    print("\nAssegno il valore 99 da index 5 a index 10 :")
    print(random_array)
    return random_array


random_array = None
while True:
    print("\nMenu:")
    print("1. Crea un array di numeri interi casuali")
    print("2. Estrarre i primi 10 elementi dell'array")
    print("3. Estrarre gli ultimi 5 elementi dell'array")
    print("4. Estrarre gli elementi dall'indice 5 all'indice 15 (escluso)")
    print("5. Estrarre ogni terzo elemento dell'array")
    print("6. Modificare gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99")
    print("7. Esci")

    choice = input("Scegli un'opzione: ")

    if choice == '1':
        random_array = crea_array1d()
    elif choice == '2':
        if random_array is not None:
            slicing_f10(random_array)
        else:
            print("Crea prima l'array!")
    elif choice == '3':
        if random_array is not None:
            slicing_l5(random_array)
        else:
            print("Crea prima l'array!")
    elif choice == '4':
        if random_array is not None:
            slicing_5to15(random_array)
        else:
            print("Crea prima l'array!")
    elif choice == '5':
        if random_array is not None:
            slicing_3th(random_array)
        else:
            print("Crea prima l'array!")
    elif choice == '6':
        if random_array is not None:
            slicing_99(random_array)
        else:
            print("Crea prima l'array!")
    elif choice == '7':
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida. Riprova.")