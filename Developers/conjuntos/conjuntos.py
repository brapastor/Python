__author__ = 'brapastor'

canasta = {'manzana','naranja','manzana','pera','naranja','banana'}
print (canasta) # muestra que se removieron los duplicados;


print('naranja' in canasta) # verificamos si existe naranja en el conjunto
print('uerba' in canasta)

a = set('adacadabra')
b = set('alacazan')

print(a) # letras unicas en a

print(a-b) # letras en a pero no en b
print(a|b) # letras en a o en b
print(a&b) # letras en a y en b
print(a ^ b) # letras en a o en b pero no ambos

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

