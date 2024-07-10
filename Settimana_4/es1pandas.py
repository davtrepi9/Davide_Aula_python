import pandas as pd

import xml.etree.ElementTree as ET

dati="""<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>"""

root=ET.fromstring(dati)

df_col = ["libro","titolo", "autore"]
righe = []
cont=0
for nodo in root:
    titolo=nodo.find("titolo").text if nodo is not None else None
    autore=nodo.find("autore").text if nodo is not None else None
    cont+=1

    righe.append({"libro":cont,"titolo":titolo,"autore":autore,})

df = pd.DataFrame(righe, columns=df_col)
print(df)

df.to_csv("libri.csv", index=False)
"""df = pd.read_csv("libri.csv")"""
df.to_html("libro1.html",index=False)