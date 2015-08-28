__author__ = 'brapastor'
# Para iterar sobre una secuencia ordenada, se utiliza la función sorted() la cual devuelve una nueva lista ordenada dejando a la original intacta.

canasta = ['manzana', 'naranja','manzana','pera','naranja', 'banana']
for f in sorted(set(canasta)):
    print(f)
