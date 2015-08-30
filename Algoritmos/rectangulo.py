__author__ = 'brapastor'

# construya un algoritmo que dados la base y la altura de un rectangulo, calcule el perimetro y la superficie del mismo


b=float(input("base del rectangulo "))
a=float(input("altura del rectangulo "))

superficie=b*a

perimetro=2*(a+b)

print("la superficie del rectangulo es",superficie)
print("la perimetro del rectangulo es",perimetro)