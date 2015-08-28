__author__ = 'brapastor'

def hacer_ingrementador(n):
    return lambda x:x+n

f= hacer_ingrementador(40)
print(f(1))