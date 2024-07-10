"""Database sarà:
-radice: <studenti>
Per ogni studente:
-Elemento <studente> con attributo id
-Elemento figlio <nome> per il nome dello studente
- Elemento figlio <corsi> che contiene elementi <corso> per ogni corso seguito dallo studente
-Elemento figlio <corso> che contiene elementi <voto> per ogni corso seguito dallo studente

Al primo avvio se il database è presente viene letto, se non è presente risulta database vuoto!
L'utente può aggiungere, eliminare o modificare uno studente, un corso o un elemento di corso"""

import xml.etree.ElementTree as ET


def crea_db():
    root = ET.Element('studenti')
    tree = ET.ElementTree(root)
    tree.write("database.xml")


def controllo_db():
    try:
        tree = ET.parse("database.xml")
        root = tree.getroot()
        return root
    except:
        print("Database vuoto/non presente\n")
        crea_db()
        print("Db creato!")

def aggiungi_elemento(root):
    contatore = 0
    studente = ET.SubElement(root, 'studente', attrib={"id": str(contatore)})
    contatore=+1
    inpnome=input("Aggiungi nome studente: ")
    nome = ET.SubElement(studente, 'nome')
    nome.text = inpnome
    corsi = ET.SubElement(studente, 'corsi')
    ncorsi = input("Inserisci quanti corsi salvare(min1): ")
    for i in range(int(ncorsi)):
        nomecorso=input("Aggiungi nome corso: ")
        corso = ET.SubElement(corsi, 'corso')
        tagcorso = ET.SubElement(corso,'nome')
        tagcorso.text=nomecorso
        valorevoto=input("Aggiungi il voto: ")
        voto = ET.SubElement(corso, 'voto')
        voto.text=valorevoto
    tree = ET.ElementTree(root)
    tree.write("database.xml")


def elimina_studente(root):

    nome = input("Che studente vuoi eliminare: ")
    for elemento in root.findall('studente'):
        if elemento.find('nome').text:
            elemento.clear()
        
    
#TESTING

#Controlla db
root=controllo_db()
#Non esiste, quindi lo creiamo facendo primo inserimento
crea_db()
#Controlliamo di nuovo

#Facciamo inserimento
aggiungi_elemento(root)
#Stampiamo
root=controllo_db()
            
"""
elimina_studente(root)

for elemento in root.findall('studente'):
    print(f"Nome : {elemento.find('nome').text}")
    print(f"Corso: {elemento.find('corso').text}")
    print(f"Voto: {elemento.find('voto').text}")"""
