import requests
import pandas as pd
import xml.etree.ElementTree as ET

contenuto = requests.get("https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml")
contenuto=contenuto.text
root=ET.fromstring(contenuto)

df_col = ["title","descrizione", "link","pubdate"]
righe = []
cont=0
for nodo in root:
    titolo=nodo.find("title").text if nodo is not None else None
    descrizione=nodo.find("description").text if nodo is not None else None
    link=nodo.find("link").text if nodo is not None else None
    pubdate=nodo.find("pubDate").text if nodo is not None else None

    righe.append({"titolo":titolo,"descrizione":descrizione,"link":link,"pubdate":pubdate})

"""channell=root.find("channel")
notizia=channell.find("item")
titolo=notizia.find("title")
descrizione=notizia.find("description")
link=notizia.find("link")
pubdate=notizia.find("pubDate")"""


df = pd.DataFrame(righe, columns=df_col)
print(df)
