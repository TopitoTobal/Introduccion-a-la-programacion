from math import sqrt
n= int(input("n: "))
factor= 1/sqrt(5)

operando1 = (1 + sqrt(5))/2
operando2 = (1 - sqrt(5))/2
resultado = factor * (operando1**n - operando2**n)

print (resultado)
