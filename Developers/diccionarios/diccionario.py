__author__ = 'brapastor'

tel = { 'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['sape']) # mostrando valor en la key sape
del tel['sape'] # eliminando clave

print(tel)
tel['irv'] =4127
print(tel)

print(list(tel.keys())) # obteniendo las keys como una lista
print(sorted(tel.keys())) # ordenando en ascendente la lista

print('guido' in tel) # comprobando si dicha key existe en tel
print('jack' not in tel)
