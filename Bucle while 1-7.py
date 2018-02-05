#coding: utf-8
num1=input("Introduce un número:")
num2=input("Introduce un número mayor que "+str(num1)+": ")
while num1>=num2:
	num2=input(str(num2)+" no es mayor que "+str(num1)+" intentalo de nuevo: ")
num3=float(input("Introduce un número entre "+ str(num1)+" y "+str(num2)+": "))
count=0
while num1<=num3<=num2:
    count+=1
    num3=float(input("Introduce un número entre "+str(num1)+" y "+str(num2)+": "))
if count==0:
    print "No ha introducido ningun número entre", num1, "y", str(num2) + "."
elif count==1:
    print "Has introducido 1 número entre", num1, "y", str(num2)+"."
else:
    print "Has introducido", count, "números entre", num1, "y", str(num2) + "."
print "Programa terminado"
