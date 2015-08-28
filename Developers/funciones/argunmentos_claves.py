__author__ = 'brapastor'


def loro(tension, estado='muerto',accion='explotar',tipo= 'azul nordico'):
    print("--este loro no va a", accion, end=' ')
    print("si le aplicas", tension, "voltios")
    print("Gran plumaje tiene el", tipo)
    print("-- esta",estado, "!")

d= {
    "tension":"cinco mil",
    "estado" :"demacrado",
    "accion": "Volar"
    }
loro(**d)