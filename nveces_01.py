#codigo: utf-8
num1=input("Introduce un numero:")
num2=0
while (num2<num1):
	num2=num2+1
	aux=input("Introduce otro numero:")
	if aux<0:
		num2=num2-1
print "Programa terminado"

num1=input("Introduce un numero:")
num2=0
suma=0
while (num2<num1):
	aux=input("Introduce otro numero:")
 	if aux>0:
		num2=num2+1
		suma=suma+num1
print "La suma es:", str(suma) + "."

