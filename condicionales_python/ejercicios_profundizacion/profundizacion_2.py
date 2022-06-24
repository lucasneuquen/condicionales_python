# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

print('*')
print('*')

print('ingrese un número:')
num_1=int(input())
res=num_1%2

if res==0:
    print('el número ingresado es PAR')
else:
    print('el número ingresado es IMPAR')

print('*******')

print('ingrese otro número:')
num_2=int(input())
res=num_2%2

if res==0:
    print('el segundo número ingresado es PAR')
else:
    print('el segundo número ingresado es IMPAR')
    
print('*******')

print('ingrese un tercer número:')
num_3=int(input())
res=num_3%2

if res==0:
    print('el tercer número ingresado es PAR')
else:
    print('el tercer número ingresado es IMPAR')


print('*')
print('*')
print('FIN DEL EJERCICIO')