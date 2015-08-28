__author__ = 'brapastor'

def ventaQueso(tipo,*argumentos,**palabrasclaves):
    print("Tiene", tipo)
    print("lo siento, nos quedamos sin", tipo)
    for arg in argumentos:
        print(arg)
    print("-" *40)
    claves = sorted(palabrasclaves.keys())
    for c in claves:
        print(c,":",palabrasclaves[c])

ventaQueso("quesillo","es muy liquido","sr",
           cliente="brayan pastor",vendedor= "joao",puesto="venta de queso argentino")