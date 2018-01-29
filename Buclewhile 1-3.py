#coding: utf-8
numero=input("Escriba un número:")
numeromayor=input("Escriba un número mayor:")
while (numero<numeromayor):
	numero=numeromayor
	numeromayor=input("Siguiente numero:")
print "Numeros escritos:", numero, "y", numeromayor	
