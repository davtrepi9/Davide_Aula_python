#Sistema Gestione Negozio

#variabili
username= ""
password= ""
persona={
    "nomeutente": username,
    "password": password
    }
c=0
a=0
token = True

maglia = {"nome" : "maglia",
          "prezzo" : 15,
          "qnt_disp" : 2
          }
felpa = {"nome" : "felpa",
          "prezzo" : 20,
          "qnt_disp" : 1
          }
jeans = {"nome" : "jeans",
          "prezzo" : 35,
          "qnt_disp" : 5
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
            c=+1
            if c==3:
                print("\nERROR ERROR ERROR TROPPI TENTATIVI CHIUSURA FORZATA")
                exit(1)

def cliente():
#Controllo se registrato, se si faccio login. Se non sono registrato faccio registrazione e ritorno alla domanda iniziale.
    c1 = input("\nSei gia registrato?(si/no) : ")
    if c1=="si":

        if login()==True :


            # Se login restituisce true entro in un nuovo menu che mi permette di effettuare il primo punto dell'esercizio(Gestione Clienti)
            while True:
             print("\nMenu:")
             print("1: Visualizza Inventario")
             print("2: Acquista prodotto")
             print("3: Esci")
             
             selection=input("\n Cosa vuoi fare ?: ")
             if selection == "1":
                 print(listainv)
             elif selection == "2":
                 print(listainv)
                 shop=input("\nQuale prodotto vuoi acquistare ?:")
                 #NON RIESCO AD AGGIORNARE LA QUANTITA DELLA LISTA ç___ç *sad* ------------ FIXATO
                 if shop == "maglia":
                     qntnuova=maglia["qnt_disp"]
                     qntnuova=qntnuova-1
                     maglia.update({"qnt_disp": qntnuova })
                     print("Hai acquistato : ")
                     print(listainv[0])
                 elif shop == "felpa":
                     qntnuova=felpa["qnt_disp"]
                     qntnuova=qntnuova-1
                     felpa.update({"qnt_disp": qntnuova })
                     print("Hai acquistato : ")
                     print(listainv[1])
                 elif shop == "jeans":
                     qntnuova=jeans["qnt_disp"]
                     qntnuova=qntnuova-1
                     jeans.update({"qnt_disp": qntnuova })
                     print("Hai acquistato : ")
                     print(listainv[2])
             elif selection == "3":
                     break
    elif c1=="no":
            #La famosa registrazione
            print("\nRegistrazione:")
            username=input("Inserisci username: ")
            persona.update({"nomeutente" : username})
            password=input("Inserisci password: ")  
            persona.update({"password" : password}) 
            print("Registrazione Effettuata con successo!")
            

def inventario():
    while True:
        print("\nMenu:")
        print("1: Visualizza articoli magazzino")
        print("2: Aggiungi articolo")
        print("3: Aggiorna articolo")
        print("4: Rimuovi articolo")
        print("5: Esci")                
        selection=input("\n Cosa vuoi fare ?: ")
        if selection == "1":
            print(listainv)
        elif selection == "2":
            nome=input("Aggiungi nome articolo: ")
            prezzo=input("Aggiungi prezzo articolo: ")
            quantita=input("Aggiungi quantita articolo: ")

            nuovoarticolo = {"nome" : nome,
                     "prezzo" : int(prezzo),
                     "qnt_disp" : int(quantita)
           }
            
            listainv.append(nuovoarticolo)

        elif selection == "3":
                    pass
            #articolomod = input("\nQuale articolo vuoi modificare? ")
            ## if articolomod == (scorri elementi della lista e fai controllo)
                    #scelta=input("Cosa vuoi modificare: ")

                    #if scelta == "nome":
                     #nuovoele=input("Inserisci nuovo nome: ")
                     #a.update({"nome": nuovoele })

                    #elif scelta == "prezzo":
                       # nuovoele=input("Inserisci nuovo prezzo: ")
                        #a.update({"prezzo": nuovoele})
                    
                    #elif scelta == "qnt_disp":
                        #nuovoele=input("Inserisci nuova quantità: ")
                        #a.update({"qnt_disp": nuovoele})
           # break
        
        elif selection == "5":
            break

           

            

def amministrazione():
    pass




# main                        
#MENU PRINCIPALE

start = input("-- Vuoi iniziare ? (si/no)-- ") 
if start == "si":
 while True:
    print("\nMenu:")
    print("1: Gestione Clienti")
    print("2: Gestione Inventario")
    print("3: Amministrazione")
    print("4: Esci")

    seleziona = input("\nCosa vuoi fare?: ")

    if seleziona =="1":
     cliente()
    elif seleziona =="2":
      inventario()
    elif seleziona =="3":
     amministrazione()
    elif seleziona =="4":
     print("-- Chiusura sistema -- ")
     break
    
else:
    print("-- Chiusura sistema -- ")
    exit(1)

#APPUNTI PER DOMANI 

#Svolto: Login-Registrazione-Primo punto
#Da Svolgere:
#1) Fix quantità sul primo punto
#2) Implementare secondo (riusare parte di codice dal primo punto) , aggiungere modifica e aggiunta di prodotti
#3) Implementare terzo