#Descrizione: Scrivi un programma che chieda all'utente la sua età. 
#Se l'età è inferiore a 18 anni, il programma dovrebbe stampare "Mi dispiace, non puoi vedere questo film".
#Altrimenti, dovrebbe stampare "Puoi vedere questo film".

x=18
eta= input("\nInserisci la tua eta' : ")

if int(eta)>=x :
    print("\nPuoi vedere questo film")
else :
    print("\nNon puoi vedere questo film")
