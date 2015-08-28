from builtins import print

cuadrados = [1,4,9,16,25]
print(cuadrados)
print(cuadrados[3])
print(cuadrados[0:])
print(cuadrados[:2])
print(cuadrados[-3:])
print(cuadrados[:]) # copia superficial de la lista

# CONCATENANDO LISTAS
print(cuadrados + cuadrados[-3:])

# modificando valor a lista
print('CUBO')
cubos = [1,8,27,65,125]
print(cubos)
cubos[3] = 64
print(cubos)
# AGREGANDO VALOR AL FINAL DE LA LISTA CON APPEND
cubos.append(216)
cubos.append(7**3)
print(cubos)

letras = ['a','b','c', 'd', 'e', 'f', 'g']
print(len(letras))
print('REMPLAZANDO VALORES EN LETRAS')
letras[2:5] = ['C','D','E']
print(letras)
letras[2:5]=[] # Asignando vacios
print(letras)
letras[:]=[]
print(letras)

#ANIDANDO LISTAS
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print(x)
print(x[0][1])
