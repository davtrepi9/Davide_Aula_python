#REALIZZATO CON AMALIA CHIARIELLO 

"""
Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 
Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni sulla matrice. 
Le operazioni disponibili includono:
1. Creare una nuova matrice 2D di dimensioni specificate con numeri casuali.
2. Estrarre e stampare la sotto-matrice centrale.
3. Trasporre la matrice e stamparla.
4. Calcolare e stampare la somma di tutti gli elementi della matrice.
5. Uscire dal programma.


Parte DUE: Andare a specializzare per aggiungere nuove operazioni:

1.Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare una seconda matrice 
delle stesse dimensioni della prima e moltiplicarle elemento per elemento e stampare il risultato.
2.Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di tutti gli elementi 
della matrice.


EXTRA:

Determinante della Matrice: Calcolare e stampare il determinante della matrice (solo se la matrice è quadrata).



Parte 3: Ulteriore Estensione del Menu Interattivo


Estendere ulteriormente il programma precedente aggiungendo nuove opzioni al menu per permettere ulteriori operazioni sulla matrice. Le nuove operazioni includono:

Calcolare la matrice inversa (se la matrice è quadrata e invertibile).
Applicare una funzione matematica a tutti gli elementi della matrice (ad esempio, sin, cos, exp).
Filtrare e visualizzare solo gli elementi della matrice che soddisfano una determinata condizione (ad esempio, maggiori di un certo valore).
RENDERE OGNI PARTE RICHIAMABILE SINGOLARMENTE
Uscire dal programma.

"""

import numpy as np

def genera(riga,colonna):
    matrice = np.random.randint(1,101, size=(riga,colonna))
    print("\nMatrice stampata: ")
    print(matrice)
    return matrice

def centrale(matrice,riga,colonna):
    if riga == 1 and colonna == 1:
        print("\n Operazione non possibile")
    elif (riga == 1 and colonna == 2) or (riga==2 and colonna==1):
        print("\n Operazione non possibile")
    else:
        centrale = matrice[1:riga,1:colonna]
        print("\nSotto-matrice centrale : ")
        print(centrale)
        return centrale

def trasposta(matrice):
    trasposta = matrice.T
    print("\nTrasposta: ")
    print(trasposta)
    return trasposta

def somma(matrice):
    som = np.sum(matrice)
    print("\n La somma degli elementi della matrice è:", som)
    return som

def moltiplica(matrice):
    matrice2 = np.random.randint(1,101, size=(riga,colonna))
    print("\nLa nuova matrice generata è:" , matrice2)
    multi = np.multiply(matrice,matrice2)
    print("\nLa moltiplicazione della matrice è: ")
    print(multi)
    return multi

def media(matrice):
    med = np.mean(matrice)
    print("\nLa media della matrice è: ", med)
    return med

def determinante(matrice, riga, colonna):
    if riga == colonna:
        deter = np.linalg.det(matrice)
        print("\nIl determinante della matrice è: ",deter)
        return deter
    else:
        print("La matrice non è quadrata ")

def inversa(matrice):
    inv = np.linalg.inv(matrice)
    print("\nL'inversa della matrice è: ")
    print(inv)
    return inv

def esponenziale(matrice):
    esp = np.exp(matrice[matrice >5])
    print("\nEsponenziale degli elementi: ")
    print(esp)
    return esp

def error():
    print("\nCrea prima l'array!")

##########################
#MAIN
##########################


matrice = None
deter = 0

while True:
    print("\nMenu:")
    print("1. Crea una matrice ")
    print("2. Estrai sottomatrice centrale ")
    print("3. Trasposta ")
    print("4. Somma degli elementi della matrice")
    print("5. Moltiplicazione Element-Wise")
    print("6. Media degli elementi della matrice")
    print("7. Determinante della matrice")
    print("8. Inversa della matrice")
    print("9. Esponenziale degli elementi")
    print("10. Esci")

    seleziona = input("Scegli un'opzione: ")
        
    if seleziona.isalpha():
            print("Errore Input ")
            break
    if seleziona.isspace():
            print("Errore Input ")

    if seleziona == '1':
        while True:
            riga = int(input("Inserire il numero di righe "))
            colonna = int(input("Inserire il numero di colonne "))
            if riga == 0 or colonna == 0:
                print("Min 2 : Input non valido")
            elif riga > 11 or colonna > 11:
                print("Max 10 : Input non valido!")
            else: break
        matrice = genera(riga,colonna)
    elif seleziona == '2':
        if matrice is not None:
            centrale(matrice,riga,colonna)
        else:
            error()
    elif seleziona == '3':
        if matrice is not None:
            trasposta(matrice)
        else:
            error()
    elif seleziona == '4':
        if matrice is not None:
            somma(matrice)
        else:
            error()
    elif seleziona == '5':
        if matrice is not None:
            moltiplica(matrice)
        else:
            error()
    elif seleziona == '6':
        if matrice is not None:
            media(matrice)
        else:
            error()
    elif seleziona == '7':
        if matrice is not None:
            deter = determinante(matrice,riga,colonna)
        else:
            error()
    elif seleziona == '8':
        if matrice is not None:
                if deter == 0 or riga != colonna:
                    print("Errore!  Determinante uguale a 0 oppure matrice non quadrata !")
                else: inversa(matrice)
        else:
            error()
    elif seleziona == '9':
        if matrice is not None:
            esponenziale(matrice)
        else:
            error()
    
    elif seleziona == '10':
        break
    else:
        print("Scelta non valida. Riprova.")
