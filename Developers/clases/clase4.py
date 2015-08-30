__author__ = 'brapastor'
#Los métodos pueden llamar a otros métodos de la instancia usando el argumento self:

class Bolsa:

    def __init__(self):
        self.datos =[]

    def agregar(self,x):
        self.datos.append(x)

    def dobleAgregar(self,x):
        self.agregar(x)
        self.agregar(x)

x = Bolsa
print(x.agregar.__class__)
