__author__ = 'brapastor'

while True:
    try:
        x = int(input("por favor ingrese un numero"))
        break
    except ValueError:
        print("opps no es valido intente nuevamente")

