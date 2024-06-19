
risposta=""

persona={
    "nomeutente": "admin",
    "password": "12345"
}

print(persona.get("nomeutente"))
print(persona.get("password"))
nu = input("\nInserisci nome utente: ")
pw = input("\nInserisci password: ")

if persona["nomeutente"] == nu :
    if persona["password"] == pw:
        print("\nBenvenuto campione <3")
else: 
       print("\nCredenziali sbagliate")

while True:
    print("\nSeleziona una domanda segreta:")
    print("1: Qual'è il tuo colore preferito?")
    print("2: Quale animale preferito?")

    seleziona = input("Seleziona: ")

    if seleziona =="1":
        add = input("Inserisci risposta segreta: ")
        risposta = add
        break
    elif seleziona =="2":
        add = input("Inserisci risposta segreta: ")
        risposta = add
        break
  

while True:
    print("\nMenu:")
    print("1: Modifica Nome Utente")
    print("2: Modifica Password")
    print("3: Esci")

    seleziona = input("Cosa vuoi fare?: ")

    if seleziona =="1":
        add = input("Inserisci nuovo nome utente: ")
        persona.update({"nomeutente": add})
    elif seleziona =="2":
        add = input("Inserisci nuova password: ")
        persona.update({"password": add})
    elif seleziona =="3":
        break

print("\n Credenziali aggiornate: ")
print(persona.get("nomeutente"))
print(persona.get("password"))



