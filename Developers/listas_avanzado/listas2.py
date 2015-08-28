__author__ = 'brapastor'

a = [66.25,333,333,1,1234,5]
print(a.count(333), a.count(66.25),a.count('x')) #devuelve el numero de veces que aparece en la lista

a.insert(2,-1) #inserta en la posicion 2 el -1
a.append(333) # inserta al final de la lista
print(a)

print(a.index(333)) #muestra el indice
a.remove(333) # remueve el valor de la lista
print(a)
a.reverse() # lista al reves
print(a)

a.sort()
print(a) # de forma ascendente

a.pop(2) # elimina el ultimo de la lista nota si no se pone la posicion elimina el ultimo
print(a)

