"""Scrivere un programma Python che ricerca e stampa gli elementi di un documento XML chesoddisfano
 determinati criteri. Considera il seguente documento XML: (file.xml)
Il programma dovrebbe cercare e stampare tutti i prodotti con un prezzo inferiore a 600."""

import xml.etree.ElementTree as ET

tree = ET.parse("file.xml")
root = tree.getroot()

for elemento in root.findall('prodotto'):
    if int(elemento.find('prezzo').text) < 600:
        print(f"{elemento.find('nome').text} ha prezzo minore di 600")
    
    