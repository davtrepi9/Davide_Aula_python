#Sistema Gestione Negozio

#variabili
username= ""
password= ""
persona={
    "nomeutente": username,
    "password": password
    }
c=0
token = True

maglia = {"nome" : "maglia",
          "prezzo" : 15,
          "qnt" : 2
          }
felpa = {"nome" : "felpa",
          "prezzo" : 20,
          "qnt" : 1
          }
jeans = {"nome" : "jeans",
          "prezzo" : 35,
          "qnt" : 5
          }

listainv = [maglia,felpa,jeans]

#funzioni
def login():
    while True:
        nu = input("\nInserisci nome utente: ")
        pw = input("\nInserisci password: ")
        if persona["nomeutente"] == nu :
            if persona["password"] == pw:
                print("\n Benvenuto!" )
                return True
            else:
                print("\nCredenziali sbagliate")
            c += 1
            if c==3:
                print("\nERROR ERROR ERROR TROPPI TENTATIVI CHIUSURA FORZATA")
                exit(1)

def cliente():
    c1 = input("\nSei gia registrato?(si/no) : ")
    if c1=="si":
        login()
        if login()==True :
            while True:
             print("\nMenu:")
             print("1: Visualizza Inventario")
             print("2: Acquista prodotto")
             print("3: Esci")
             
             selection=input("\n Cosa vuoi fare ?: ")
             if selection == 1:
                 print(listainv)
             elif selection == 2:
                 print(listainv)
                 shop=input("\nQuale prodotto vuoi acquistare ?:")
                 
                 if shop == "maglia":
                     maglia.update({int("qnt") : int("qnt")-1})
                     print("Hai acquistato ",listainv[maglia])
                 elif shop == "felpa":
                     maglia.update({int("qnt") : int("qnt")-1})
                     print("Hai acquistato ", listainv[felpa])
                 elif shop == "felpa":
                     jeans.update({int("qnt") : int("qnt")-1})
                     print("Hai acquistato "), listainv[jeans]
                 elif shop == "3":
                     break
    elif c1=="no":
            print("\nRegistrazione:")
            username=input("Inserisci username: ")
            persona.update({"nomeutente" : username})
            password=input("Inserisci password: ")  
            persona.update({"password" : password}) 
            print("Registrazione Effettuata con successo!")

def inventario():
    pass

def amministrazione():
    pass




                         
            
start = input("-- Vuoi iniziare ? (si/no)-- ") 
if start == "si":
 print("\nMenu:")
 print("1: Gestione Clienti")
 print("2: Gestione Inventario")
 print("3: Amministrazione")
 print("4: Esci")

seleziona = input("Cosa vuoi fare?: ")

if seleziona =="1":
     cliente()
elif seleziona =="2":
    inventario()
elif seleziona =="3":
     amministrazione()
elif seleziona =="4":
     print("-- Chiusura sistema -- ")
     exit(1)
    
else:
    print("-- Chiusura sistema -- ")
