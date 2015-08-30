__author__ = 'brapastor'
#La modificación de nombres es útil para dejar que las subclases sobreescriban los métodos sin
# romper las llamadas a los métodos desde la misma clase. Por ejemplo:

class Mapeo:
    def __init__(self,iterable):
        self.lista_de_items = []
        self.__actualizar(iterable)

    def actualizar(self,iterable):
        for item in iterable:
            self.lista_de_items.append(item)

    __actualizar = actualizar() # copia ptivada del actulizar() original

class SubClaseMapeo:

    def actualizar(self,keys,values):
        # provee una nueva signatura para actualizar()
        #pero no rompe __init__()
        for item in zip(keys,values):
            self.lista_de_items.append(item)
