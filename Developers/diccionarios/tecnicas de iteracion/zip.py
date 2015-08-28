__author__ = 'brapastor'

#Para iterar sobre dos o más secuencias al mismo tiempo, los valores pueden emparejarse con la función zip().
preguntas = ['nombre','objetivo','color favorito']
respuestas = ['lancelot','el santo grial','azul']

for p, r in zip(preguntas,respuestas):
    print('cual es tu {0} {1}.'.format(p,r))
