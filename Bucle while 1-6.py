#coding: utf-8
num1=float(input("Escriba un limite: "))
while num1<=0:
	num1=float(input("Debe ser mayor que 0 intente de nuevo:"))
num2=float(input("Escriba un número: "))
suma=0
suma+=num2
while suma<num1:
    num2=float(input("Escriba otro número: "))
    suma+=num2
print "Se ha superado el limite, la suma de los numeros positivos es:", str(suma) + "."
print "Programa terminado"
