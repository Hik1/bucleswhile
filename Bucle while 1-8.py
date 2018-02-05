#coding: utf-8
num1=input("Introduce un número par: ")
while num1%2!=0:
    num1=input(str(num1) + " no es un número par. Intentalo de nuevo: ")
count=1
r=raw_input("¿Quiere escribir otro número par? (S/N) ")
while r=="S":
    num1=input("Escriba un número par: ")
    while num1%2!= 0:
        num1=input(str(num1)+"no es un número par. Intentelo de nuevo: ")
    count+=1
    r=raw_input("¿Quiere escribir otro número par? (S/N) ")
if count==0:
    print "No has escrito un número par"
elif count==1:
    print "Has escrito 1 número par"
else:
    print "Ha escrito", count, "numeros pares."
print "Programa terminado" 
