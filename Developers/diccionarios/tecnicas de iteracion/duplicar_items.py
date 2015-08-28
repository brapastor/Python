__author__ = 'brapastor'
palabras= ['gato','ventana','defenestrar']
for p in palabras[:]:
    if len(p)>6:
        palabras.insert(0,p)

print(palabras)
