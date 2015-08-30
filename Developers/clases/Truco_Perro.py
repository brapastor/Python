__author__ = 'brapastor'

class Perro:
    def __init__(self,nombre):
        self.nombre = nombre
        self.trucos = []      #crea una nueva lista vacia para cada perro. Manera correcta no en los atributos

    def agregar_truco(self,truco):
        self.trucos.append(truco)

d = Perro('nombre')
e = Perro('chop')

d.agregar_truco('Girar')

e.agregar_truco('hacerse el muerto')

print(d.trucos)
print(e.trucos)



