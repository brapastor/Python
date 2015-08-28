from builtins import print

__author__ = 'brapastor'

while True:
    try:
        x= int(input("por favor ingrese un numero"))
        break
    except ValueError:
        print("Ooosps: no era valido. Itente nuevamente")

