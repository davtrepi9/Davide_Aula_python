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

def genera_matrice():
    matrice = np.random.randint(1, 101, size=(6,6))
    print("\nMatrice 6x6 generata : ")
    print(matrice)
    return matrice

def centrale(matrice):
    centrale = matrice[1:5,1:5]
    print("\nSotto-matrice centrale : ")
    print(centrale)
    return centrale

def inverti(matrice):
    inversa = matrice[::-1]
    print("\nMatrice con righe invertite : ")
    print(inversa)
    return inversa

def diagonal(matrice):
    diagonale = np.diag(matrice)
    print("\nDiagonale della matrice : ")
    print(diagonale)

def multipli(inversa):
    if inversa is not None:
        inversa[inversa % 3 == 0] = -1
        print("\nInversa con multipli di 3 cambiati a -1 : ")
        print(inversa)
        return inversa
    else: print("Matrice assente")



#MAIN

matrice_originale = None
matrice_centrale = None
matrice_invertita = None

while True:
        print("\nMenu:")
        print("1. Genera matrice 6x6")
        print("2. Estrai sotto-matrice centrale 4x4")
        print("3. Inverti righe della sotto-matrice")
        print("4. Estrai diagonale della matrice invertita")
        print("5. Sostituisci multipli di 3 con -1 nella matrice invertita")
        print("6. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            matrice_originale = genera_matrice()
        elif scelta == '2':
            if matrice_originale is not None:
                matrice_centrale = centrale(matrice_originale)
            else:
                print("Genera prima la matrice originale!")
        elif scelta == '3':
            if matrice_centrale is not None:
                matrice_invertita = inverti(matrice_centrale)
            else:
                print("Estrai prima la sotto-matrice centrale!")
        elif scelta == '4':
            if matrice_invertita is not None:
                diagonal(matrice_invertita)
            else:
                print("Inverti prima le righe della sotto-matrice!")
        elif scelta == '5':
            if matrice_invertita is not None:
                multipli(matrice_invertita)
            else:
                print("Inverti prima le righe della sotto-matrice!")
        elif scelta == '6':
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida. Riprova.")