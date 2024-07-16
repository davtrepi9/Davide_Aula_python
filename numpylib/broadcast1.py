"""Esercizio 1: Somma e Media di Elementi

Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.

Calcolare e stampare la somma di tutti gli elementi dell'array.

Calcolare e stampare la media di tutti gli elementi dell'array."""

import numpy as np

# Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
def genera():
    array = np.random.randint(1, 101, size=15)
    print("\nArray di numeri interi casuali compresi tra 1 e 100:")
    print(array)
    return array

#Somma degli elementi dell'array
def somma_ele(array):
    somma = np.sum(array)
    print(f"Somma matrice random: {somma}")
    return somma

#Media degli elementi dell'array
def media_ele(array):
    media = np.mean(array)
    print(f"Media degli elementi: {media}")
    return media

random_array = None

while True:
    print("\nMenu:")
    print("1. Crea un array di numeri interi casuali")
    print("2. Somma")
    print("3. Media")
    print("4. Esci")

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
            somma_ele(random_array)
        else:
            print("Crea prima l'array!")
    elif seleziona == '3':
        if random_array is not None:
            media_ele(random_array)
        else:
            print("Crea prima l'array!")
    elif seleziona == '4':
        break
    else:
        print("Scelta non valida. Riprova.")