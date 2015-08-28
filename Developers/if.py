from builtins import print

x = int(input("ingresar un entero, por favor"))
if x <0 :
    x=0
    print('negativo cambiado a cero')
elif x == 0:
    print('cero')
elif x ==1:
    print('simple')
else:
    print('mas')

