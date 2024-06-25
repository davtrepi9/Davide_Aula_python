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

def palindromo2(inp):
    inversa=list(reversed(inp))
    return True if list(inp) == inversa else False

def palindromo3(inp):
    inversa="".join(reversed(inp))
    return True if inp == inversa else False

s=input("Inserisci stringa: ")

print("1: Palindromo: ",palindromo(s.lower()))
print("2: Palindromo: ",palindromo2(s.lower()))
print("3: Palindromo: ",palindromo3(s.lower()))