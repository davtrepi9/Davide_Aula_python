from random import *
token=True

def genera():
    numerogenerato=randint(1,100)
    return numerogenerato



#main
ngenerato=genera()
print(ngenerato)
while token:
 previsione=int(input("Indovina il numero generato: "))
 if previsione==ngenerato:
    print("HAI INDOVINATO")
    token=False
 elif previsione>ngenerato:
    print("Il numero da indovinare è più piccolo")
    scelta=input("Vuoi continuare? (si/no)")
    if scelta=="si":
       pass
    elif scelta=="no":
       token=False
 elif previsione<ngenerato:
    print("Il numero da indovinare è più grande")
    scelta=input("Vuoi continuare? (si/no)")
    if scelta=="si":
       pass
    elif scelta=="no":
       token=False
    