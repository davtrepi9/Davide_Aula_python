import json
import requests

def converti_dict_json(dizionario):
    json2 = json.dumps(dizionario)
    return json2

def converti_json_dict(risposta):
    dizionario_json = json.loads(risposta)
    return dizionario_json

def request_citta(citta):
    risposta = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={citta}&count=1&language=it&format=json").text
    return risposta

def get_meteo(lat, lon, giorni):
    #creo un dizionario coi parametri che voglio (vedi da api.open-meteo i parametri che voglio)
    params = {
        'latitude': lat,
        'longitude': lon,
        'hourly': 'temperature_2m,windspeed_10m,precipitation',
        'timezone': 'auto',
        'forecast_days': giorni
    }
    #Faccio la get dei parametri che voglio io (params)
    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
    #Restituisco la get in json
    return response.json()

def stampa_previsioni(meteo, giorni,citta):
    print(f"METEO di : {citta}")
    #CICLO PER I GIORNI INSERITI
    for elemento in range(giorni):
        print(f"Giorno {elemento + 1}:")
    #CICLO PER LE ORE (24 ore)
        for ora in range(24):
            print(f"  Ora {ora}:00")
            #ESTRAGGO DA METEO -> HOURLY -> TEMPERATURA_2M o WINDSPEED o PRECIPITATION -> e come indice ORA(elemento che itero)
            print(f"    Temperatura: {meteo['hourly']['temperature_2m'][ora]} °C")
            print(f"    Velocità del vento: {meteo['hourly']['windspeed_10m'][ora]} km/h")
            print(f"    Precipitazioni: {meteo['hourly']['precipitation'][ora]} mm")
        print(" -- -- -- ")

def inserisci_citta():
    citta = input("Inserisci il nome della città: ")
    citta_js = request_citta(citta)
    dict = converti_json_dict(citta_js)
    if 'results' in dict and len(dict['results']) > 0:
        lat = dict['results'][0]['latitude']
        lon = dict['results'][0]['longitude']
        print(f"Coordinate di {citta}: latitudine {lat}, longitudine {lon}")
    else:
        print(f"Non è stato possibile trovare : {citta}")
        return

    giorni = int(input("Quanti giorni vuoi vedere? (1, 3, 7): "))
    if giorni == 2 or giorni == 4 or giorni == 5 or giorni == 6:
        exit("Error")
    else: 
        meteo = get_meteo(lat, lon, giorni)
        stampa_previsioni(meteo, giorni,citta)

inserisci_citta()