import xml.etree.ElementTree as ET

# Funzione per aggiungere un nuovo libro al documento XML
def aggiungi_libro(xml_file, titolo, autore):
    # Analizza il documento XML
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Crea un nuovo elemento libro
    nuovo_libro = ET.SubElement(root, 'libro')
    titolo_element = ET.SubElement(nuovo_libro, 'titolo')
    titolo_element.text = titolo
    autore_element = ET.SubElement(nuovo_libro, 'autore')
    autore_element.text = autore
    
    # Salva il documento XML modificato
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)
    print(f"Il libro '{titolo}' di '{autore}' è stato aggiunto con successo.")



xml_file = 'libro.xml'
    
titolo = input("Inserisci il titolo del libro: ")
autore = input("Inserisci l'autore del libro: ")

aggiungi_libro(xml_file, titolo, autore)

