#coding: utf-8
num1=float(input("Escriba el limite: "))
while num1<= 0:
    num1=float(input("El limite debe ser mayor que 0. Intente de nuevo: "))
num2=float(input("Escriba un número: "))
suma=0
suma+=num2
while suma<num1:
    num2=float(input("Escriba otro número: "))
    suma+=num2
print("Suma de números positivos:", str(suma)+".")
print("Programa terminado")