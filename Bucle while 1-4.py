#coding: utf-8
num1=input("Escriba la cantidad de números positivos: ")
num2=input("Escriba un número: ")
x=1
if num2>0:
    num3=1
else:
    num3=0
while num3<num1:
    num2=input ("Escriba otro número:")
    if num2>0:
        num3+=1
    x+=1
if num3==1:
    print "Ha escrito 1 número positivo."
else:
    print "Ha escrito", x, "números,", num1, "de ellos positivos."
print "Programa terminado"
