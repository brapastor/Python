__author__ = 'brapastor'

s= 'salida mundo'
print(str(s))
print(repr(s))
print(str(1/7))

hola = 'hola mundo\n'
holas = repr(hola)
print(holas)

for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    #notar el uso de 'end' en la linea anterior
    print(repr(x*x*x).rjust(4))
