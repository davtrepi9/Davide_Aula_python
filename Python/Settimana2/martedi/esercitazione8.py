#Scrivete un programma che utilizza il cifrario di Cesare per criptare una
#parola o decriptarla.
#Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
#ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
#sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
#di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
#una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
#Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
#conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
#di posti corrispondente alla chiave.


def cifratura(testo,key):
     cifrato = ""
     for x in testo:
         cifrato += chr((ord(x)+key-97) % 26+97)
     return cifrato

def decifratura(testo,key):
     cifrato = ""
     for x in testo:
         cifrato += chr((ord(x)-key-97) % 26+97)
     return cifrato
   
key=int(input("Inserisci la chiave di cifratura: "))
testo = input("Inserisci il testo da cifrare: ")
value1=cifratura(testo,key)
print("Criptato: ")
print(value1)
print("Decriptato: ")
print(decifratura(value1,key))

