
def fib(n):
    """EScribir la serie fibonnacci hasta n. """
    a,b = 0,1
    while a<n:
        print(a, end=' ')
        a,b =  b, a+b
        print()

f = fib
print(f(100))