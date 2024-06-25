#Scrivete un programma che utilizza una funzione che accetta
#come parametro una stringa passata dall’utente e restituisce in
#risposta se è palindroma o no.
#Esempio:
#‘I topi non avevano nipoti’ è palindroma
#‘Ai rimpianti rimediamo Maria’ è palindroma
#‘Ciao’ non è palindroma


def palindromo(inp):
    inversa=inp[::-1]
    return True if inp == inversa else False


s=input("Inserisci stringa: ")
print(palindromo(s.lower()))