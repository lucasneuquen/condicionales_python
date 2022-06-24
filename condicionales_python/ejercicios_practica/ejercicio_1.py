# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
from distutils.command.clean import clean
from turtle import clear


numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if numero_1>numero_2:
    print('* El numero ingresado mayor es el primero que ha ingresado: ',numero_1)
else:
    print('* El numero ingresado mayor es el segundo que ha ingresado: ',numero_2)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso
if numero_1>0:
    print('* El primer número que ha ingresado: ',numero_1, ' es un número positivo')
elif numero_1==0:
    print('* El primer número que ha ingresado: ',numero_1, ' es cero')
else:
    print('* El primer número que ha ingresado: ',numero_1, ' es un número negativo')

print('*')
print('*')
# Verifique si el numero_1 es mayor a 0 y menor a 100
if numero_1>0 and numero_1<100:
    print('el primer número ingresado es mayor a 0 y menor a 100')
    print('esta condición SI se ha cumplido')
else:
    print('esta condición NO se ha cumplido ya que el primer número está fuera del rango entre 0 y 100')
# Imprima en pantalla si se cumple o no la condición

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición
print('*')
 
print('*')
 
if numero_1<10 or numero_2>-2:
    print('la condición SI se cumple ya que el primer numero es menor a 10 y/o el segundo número es mayor a -2')
else:
    print('la condición NO se cumple ya que ambas partes son FALSAS')
    
print('*')

print('FIN DEL EJERCICIO')
