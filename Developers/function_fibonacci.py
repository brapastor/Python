def fib2 (n):
    """
    DEVUELVE UNA LISTA CONTENIENDO LA SERIE DE FIBONACCI HASTA N
    :param n:
    :return:
    """
    result =[]
    a,b = 0,1
    while(a<n):
        result.append(a)
        a,b = b, a+b
    return print(result)

fib2(100)

