

def area_triangolo(base,altezza):
    calcolo=base*altezza // 2
    return calcolo

def area_rettangolo(base,altezza):
    calcolo=base*altezza
    return calcolo

def area_quadrato(lato):
    calcolo=lato*lato
    return calcolo

li=[]
risultato=0

while True:
    print("\nMenu:")
    print("1: Area Triangolo")
    print("2: Area Quadrato")
    print("3. Area Rettangolo")
    print("4. Visualizza Lista Risultati")
    print("5. Esci")

    seleziona = input("Cosa vuoi fare: ")
    
    
    if seleziona=="1":
     b = int(input("Inserisci base: "))
     h = int(input("Inserisci altezza: "))
     risultato=area_triangolo(b,h)
     li.append(risultato)
     print(risultato)
 
    if seleziona=="2":
     l = int(input("Inserisci lato: "))
     risultato=area_quadrato(l)
     li.append(risultato)
     print(risultato)
    
    if seleziona=="3":
     ba = int(input("Inserisci base: "))
     ha = int(input("Inserisci altezza: "))
     risultato=area_rettangolo(ba,ha)
     li.append(risultato)
     print(risultato)
   
    if seleziona=="4":
       print("LISTA: ")
       for ele in li:
          print(ele)
    
    if seleziona=="5":
       break
