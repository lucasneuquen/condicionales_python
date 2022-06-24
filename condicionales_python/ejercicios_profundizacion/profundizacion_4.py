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

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio
print('***')

print('palabra 1:')
pal_1=(input())
print('ingrese palabra 2:')
pal_2=(input())
print('ingrese palabra 3:')
pal_3=(input())

#comienza proceso para determinar tamaños según longitud
if len(pal_1)>len(pal_2):
    if len(pal_1)>len(pal_3):
        long_mayor=pal_1
        if len(pal_2)>len(pal_3):
            long_media=pal_2
            long_menor=pal_3
        else:
            long_medio=pal_3
            long_menor=pal_2
    else:
        long_mayor=pal_3
        long_media=pal_1
        long_menor=pal_2
else:
    if len(pal_1)>len(pal_3):
        long_media=pal_1
        long_mayor=pal_2
        long_menor=pal_3
    else:
        long_menor=pal_1
        
        if len(pal_2)>len(pal_3):
            long_media=pal_2
            long_menor=pal_3
        else:
            long_medio=pal_3
            long_menor=pal_2

#comienza proceso para determinar orden alfabético
#usa la misma estructura que se usó para tamaños

if pal_1>pal_2:
    if pal_1>pal_3:
        pal_mayor=pal_1
        if pal_2>pal_3:
            pal_media=pal_2
            pal_menor=pal_3
        else:
            pal_media=pal_3
            pal_menor=pal_2
    else:
        pal_mayor=pal_3
        pal_media=pal_1
        pal_menor=pal_2
else:
    if pal_1>pal_3:
        pal_media=pal_1
        pal_mayor=pal_2
        pal_menor=pal_3
    else:
        pal_menor=pal_1
        
        if pal_2>pal_3:
            pal_mayor=pal_2
            pal_media=pal_3
        else:
            pal_mayor=pal_3
            pal_media=pal_2
print('*******')
print('ingrese 1 para ordenar alfabeticamente las palabras ingresadas o 2 para ordenarlas por longitud de menor a mayor')
opcion=int(input())

if opcion==1:
    print('Eligió ordenar las palabras alfabeticamente:')
    print('* ',pal_menor)
    print('* ',pal_media)
    print('* ',pal_mayor)
elif opcion>2 or opcion<0:
    print('el numero ingresado es incorrecto, debe ser 1 o 2')
else:
    print('Eligió ordenar las palabras por longitud:')
    print('* ',long_menor)
    print('* ',long_media)
    print('* ',long_mayor)

print('*****')
print('fin del ejercicio')