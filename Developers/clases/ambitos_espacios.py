from builtins import print

__author__ = 'brapastor'

def prueba_ambitos():
    def hacer_local():
        algo = "algo local"

    def hacer_nonlocal():
        nonlocal algo
        algo = "algo no local"

    def hacer_global():
        global algo
        algo= "algo global"

    algo = "algo de prueba"
    hacer_local()
    print("luego de la asignacion local:",algo)
    hacer_nonlocal()
    print("luego de la asignacion no local:", algo)
    hacer_global()
    print("Luego de la aignacion global:",algo)

prueba_ambitos()
print("in global scope:", algo)

