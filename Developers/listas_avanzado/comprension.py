__author__ = 'brapastor'
cuadrados = []

for x in range(10):
    cuadrados.append(x**2)

print(cuadrados)

cuadrados2 = [x ** 2 for x in range(10)]

print(cuadrados2)

comparacion = [(x,y) for x in [1,2,3] for y in [3,1,4] if x !=y]
print(comparacion)

vec = [-4,-2,0,2,4]
print([x*2 for x in vec])
print([x*2 for x in vec if x >= 0])

#Aplica una funcion a todos los elementos
print([abs(x) for x in vec]) # negativos a positivos


#LLama un metodo a cada elemento
frutafresca = ['banana     ','mora      ','maracuya      ']
print([arma.strip() for arma in frutafresca]) # quita los espacios

#crea una lista de tuplas de dos como (número, cuadrado)
print([(x,x**2) for x in range(6)])

#APLANAR UNA LISTA USANDO COMPRESION DE LISTAS CON DOS FOR
vecc= [[1,2,3],[4,5,6],[7,8,9]]

print([num for elem in vecc for num in elem])

matriz = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(list(zip(*matriz)))