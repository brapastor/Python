__author__ = 'brapastor'

def pedir_confirmacion(prompt, reintentos = 4, queja= 'si o no, por favor'):
    while True:
        ok= input(prompt)
        if ok in ('s','S','si','Si','SI'):
            return True
        if ok in ('n','no','No', 'NO'):
            return False
        reintentos =  reintentos-1
        if reintentos <0:
            raise OSError('usuario duro')
        print(queja)

pedir_confirmacion('')