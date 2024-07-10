"""Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in
caso non fosse presente vi permetterà di catturarlo salvando il numero identificativo, nome, abilità, xp(punti esperienza),peso
e altezza.
(Sul sistema API sono presenti poco più di 1000 pokemon)"""

import json
import requests
from random import randint

def converti_dict_json(dizionario):
    json2 = json.dumps(dizionario)
    return json2

def converti_json_dict(risposta):
    dizionario_json = json.loads(risposta)
    return dizionario_json

def request_pokemon(numero):
    db = requests.get(f"https://pokeapi.co/api/v2/pokemon/{numero}")
    return db.json()

def stampa_pokedex(db):
            #FORMATTO IL PESO
            peso = float(db['weight'])
            peso = peso/10


            print(f"Pagina pokedex:" )
            print(f"    Nome: \t{db['name']}")
            print(f"    ID: \t{db['order']}")
            print(f"    Abilità: ")
            for elemento in db['abilities']:
                nome_abilita = elemento['ability']['name']
                print(f"\t{nome_abilita}")
            print(f"    Exp Base: \t{db['base_experience']}")
            print(f"    Peso: \t{peso}  kg")
            print(f"    Altezza: \t{db['height']}0  cm")
            print(" -- -- -- ")

def genera_casuale():
    scelta = randint(1,1302)
    return scelta



casuale = genera_casuale()
db=request_pokemon(casuale)
stampa_pokedex(db)

