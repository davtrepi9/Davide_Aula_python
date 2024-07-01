
class Punto:                         # dichiaro la classe
 x = 0                # attributo di istanza
 y = 0             # attributo di istanza

 def nuovo(self, dx,dy):               # metodo di istanza
    self.x = dx
    self.y = dy
    print(self.x)
    print(self.y)
    
 def distanza_da_origine(self):
  if self.x == 0 and self.y == 0:
    print("Nessuna distanza")
  else:
    print("Distanza : ")
    print(self.x,self.y)


nuovopunto = Punto()
nuovopunto.nuovo(0,2)
nuovopunto.distanza_da_origine()
