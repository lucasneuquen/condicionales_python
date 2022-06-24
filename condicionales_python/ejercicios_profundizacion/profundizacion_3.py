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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''
print('************')
print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('***')

print('ingrese temperatura 1:')
temp_1=float(input())
print('ingrese temperatura 2:')
temp_2=float(input())
print('ingrese temperatura 3:')
temp_3=float(input())

if temp_1>temp_2:
    if temp_1>temp_3:
        mayor=temp_1
        if temp_2>temp_3:
            medio=temp_2
            menor=temp_3
        else:
            medio=temp_3
            menor=temp_2
    else:
        medio=temp_1
        menor=temp_2
        mayor=temp_3
else:
    if temp_1>temp_3:
        medio=temp_1
        mayor=temp_2
        menor=temp_3
    else:
        menor=temp_1
        if temp_2>temp_3:
            medio=temp_3
            mayor=temp_2
        else:
            medio=temp_2
            mayor=temp_3
if menor==temp_1:
    a=1
elif menor==temp_2:
    a=2
else:
    a=3

if mayor==temp_1:
    b=1
elif mayor==temp_2:
    b=2
else:
    b=3
    
print('La temperatura mas baja es: ',menor, ' y es la temperatura número: ',a)

print('La temperatura más alta es: ', mayor, ' y es la temperatura número: ',b)

promedio=(temp_1+temp_2+temp_3)/3
print('****')
print('El promedio de las temperaturas ingresadas es de: ', promedio)

print('****')
print('FIN DEL EJERCICIO')
print('****')