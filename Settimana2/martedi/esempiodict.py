utenti = {"id1":{"nome":"tommaso","cognome":"muraca", "indirizzo":"via roma"},
"id2":{"nome":"Giovanni","cognome":"Rossi"},
"id3":{"cognome":"Bianchi"}}

for id in utenti:
 print(f"nome utente '{utenti[id].get('nome','nome non presente')}',
      indirizzo '{utenti[id].get('indirizzo','indirizzo non presente')}'")



lista_voti=["1","2","3"]

lista_voti_int=[int(voto) for voto in lista_voti]

print(lista_voti_int)