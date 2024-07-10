import xml.etree.ElementTree as ET

# Lista di studenti
studenti = [
    {'nome': 'Alice', 'eta': '22'},
    {'nome': 'Bob', 'eta': '25'},
    {'nome': 'Charlie', 'eta': '20'}
]

# Crea l'elemento radice
root = ET.Element('studenti')

# Aggiungi gli studenti all'elemento radice
for elemento in studenti:
    studente = ET.SubElement(root, 'studente')
    nome = ET.SubElement(studente, 'nome')
    nome.text = elemento['nome']
    eta = ET.SubElement(studente, 'eta')
    eta.text = elemento['eta']

tree = ET.ElementTree(root)

tree.write("studenti.xml")
