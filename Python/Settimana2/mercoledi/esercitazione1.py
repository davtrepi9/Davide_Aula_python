#Scrivete un programma che genera 5 numeri casuali e li salva su un file, l’utente dovrà
#cercare di indovinarne almeno 2 oppure avrà perso.
from random import *
lista=[]
x=0

def genera():
  n=5
  x=0
  for a in range(n):
    nuovo=randint(1,100)
    if x==nuovo:
       n=n+1
    else:
       x=nuovo
       lista.append(str(x))
  return lista
def indovinanumeri(n1,n2):
    token=False
    token2=False
    with open("file.csv","r") as file:
        f = file.read()
        listafile = f.split()
        print(listafile)

        for i in listafile:
            if n1==i: 
               token=True 
               break 
            else: token=False
        for i2 in listafile:
           if n2==i:
              token2=True
              break
           else: token2=False
        
        if token==True and token2==True:
           return True
        else: 
           return False

def inserisci():
    with open("file.csv","a+") as file:
     print(genera())
     file.write(",".split((" ",lista))) 
     return True    

n1=input("Inserisci il primo numero: ")
n2=input("Inserisci il secondo numero: ")

inserisci()
risultato=indovinanumeri(n1,n2)
if risultato:
    print("Hai vinto! ")
else:
    print("Hai perso! ")
    





