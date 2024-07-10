"""Scrivere un programma Python che analizza un documento XML e stampa le informazioni desiderate.
Il programma dovrebbe analizzare il documento XML e stampare i nomi e le età degli studenti.
Infine salvate l'xml su file"""

import xml.etree.ElementTree as ET

# Definisci la stringa XML
xml_data = '''<studenti>
<studente>
<nome>Alice</nome>
<eta>22</eta>
</studente>
<studente>
<nome>Bob</nome>
<eta>25</eta>
</studente>
</studenti>
'''

# Parsa il documento XML
root = ET.fromstring(xml_data)

# Estrai e stampa le informazioni desiderate
for studente in root.findall('studente'):
    nome = studente.find('nome').text
    eta = studente.find('eta').text
    print(f'Nome: {nome}, Età: {eta}')

# Salva l'XML su file
tree = ET.ElementTree(root)
tree.write('studenti.xml')