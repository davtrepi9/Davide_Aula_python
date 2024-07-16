"""Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.

Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).

Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0).

Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore."""


import numpy as np

# Crea un array NumPy 2D di 20 numeri sequenziali da 1 a 25.
def genera():
    matrice = np.random.randint(10,51, size=(4,4))
    print("\nArray 4x4 numeri casuali interi tra 10 e 50:")
    print(matrice)
    return matrice

# Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).
def stampa_ele(matrice):
    indice_riga=np.array([0,1,2,3])
    indice_colonna=np.array([1,3,2,0])
    print("\nElementi selezionati: ")
    print(matrice[indice_riga,indice_colonna])
    return indice_colonna,indice_riga

# Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0)
def stampa_righed(matrice):
    indice_disp = matrice[0::2]
    print("Righe dispari della matrice:")
    print(indice_disp)

#Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore
def mod_ele(matrice, indice_riga, indice_colonna):
    matrice[indice_riga, indice_colonna] += 10
    print("Matrice modificata:")
    print(matrice)
    return matrice

random_array = None

while True:
    print("\nMenu:")
    print("1. Crea una matrice 4x4")
    print("2. Estrai elementi con indice (0, 1), (1, 3), (2, 2) e (3, 0)")
    print("3. Estrai righe dispari")
    print("4. Modifica e aggiungi 10 agli elementi dell'indice precedente")
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
            indice_riga,indice_colonna=stampa_ele(random_array)
        else:
            print("Crea prima l'array!")
    elif seleziona == '3':
        if random_array is not None:
            stampa_righed(random_array)
        else:
            print("Crea prima l'array!")
    elif seleziona == '4':
         if random_array is not None:
            mod_ele(random_array,indice_riga,indice_colonna)
    elif seleziona == '5':
        break
    else:
        print("Scelta non valida. Riprova.")