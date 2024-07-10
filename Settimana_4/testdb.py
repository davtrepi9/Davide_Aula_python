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
    print("Database creato.")
    return root

def carica_db():
    try:
        tree = ET.parse("database.xml")
        root = tree.getroot()
        return root
    except:
        print("Database vuoto/non presente\n")
        crea_db()
        print("Database creato!")

def aggiungi_studente(root):
    id_studente = len(root)
    studente = ET.SubElement(root, 'studente', attrib={"id": str(id_studente)})
    inpnome = input("Aggiungi nome studente: ")
    nome = ET.SubElement(studente, 'nome')
    nome.text = inpnome
    corsi = ET.SubElement(studente, 'corsi')
    while True:
        aggiungi_corso = input("Vuoi aggiungere un corso per lo studente? (s/n): ").lower()
        if aggiungi_corso == 's':
            aggiungi_corso_element(corsi)
        else:
            break
    tree = ET.ElementTree(root)
    tree.write("database.xml")
    

def aggiungi_corso_element(corsi):
    nomecorso = input("Aggiungi nome corso: ")
    corso = ET.SubElement(corsi, 'corso', attrib={"nome": nomecorso})
    valorevoto = input("Aggiungi il voto: ")
    voto = ET.SubElement(corso, 'voto')
    voto.text = valorevoto

def elimina_studente(root):
    id_studente = input("Inserisci l'id dello studente da eliminare: ")
    for studente in root.findall('studente'):
        if studente.get('id') == id_studente:
            studente.clear()
            print(f"Studente con id {id_studente} eliminato.")
            break
    else:
        print(f"Nessuno studente trovato con id {id_studente}.")
    tree = ET.ElementTree(root)
    tree.write("database.xml")

def modifica_studente(root):
    id_studente = input("Inserisci l'id dello studente da modificare: ")
    for studente in root.findall('studente'):
        if studente.get('id') == id_studente:
            nuovo_nome = input("Inserisci il nuovo nome dello studente: ")
            studente.find('nome').text = nuovo_nome
            while True:
                modifica_corso = input("Vuoi modificare i corsi dello studente? (s/n): ").lower()
                if modifica_corso == 's':
                    modifica_corso_element(studente.find('corsi'))
                else:
                    break
            break
    else:
        print(f"Nessuno studente trovato con id {id_studente}.")
    tree = ET.ElementTree(root)
    tree.write("database.xml")

def modifica_corso_element(corsi):
    nome_corso = input("Inserisci il nome del corso da modificare: ")
    for corso in corsi.findall('corso'):
        if corso.get('nome') == nome_corso:
            nuovo_voto = input("Inserisci il nuovo voto per il corso: ")
            corso.find('voto').text = nuovo_voto
            print(f"Corso {nome_corso} aggiornato.")
            break
    else:
        print(f"Nessun corso trovato con nome {nome_corso}.")


def stampa_studenti(root):
    for studente in root.findall('studente'):
        id_studente = studente.get('id')
        nome = studente.find('nome').text
        print(f"Studente ID: {id_studente}, Nome: {nome}")
        corsi = studente.find('corsi')
        for corso in corsi.findall('corso'):
            nome_corso = corso.get('nome')
            voto = corso.find('voto').text
            print(f"  Corso: {nome_corso}, Voto: {voto}")
        print()

def main():
    root = carica_db()
    while True:
        print("\n1. Aggiungi studente")
        print("2. Elimina studente")
        print("3. Modifica studente")
        print("4. Stampa studenti")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione: ")
        if scelta == '1':
            aggiungi_studente(root)
        elif scelta == '2':
            elimina_studente(root)
        elif scelta == '3':
            modifica_studente(root)
        elif scelta == '4':
            stampa_studenti(root)
        elif scelta == '5':
            break
        else:
            print("Opzione non valida. Riprova.")

main()