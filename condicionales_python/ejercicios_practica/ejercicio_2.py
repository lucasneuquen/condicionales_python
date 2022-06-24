# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda
if texto_1>texto_2:
    print('la primera palabra ingresada es mayor que la segunda: ',texto_1)
else:
    print('la segunda palabra ingresada es mayor que la primera: ', texto_2) #no comparé si ambas palabras son
                                                                                #iguales pero dsp si lo tuve en cuenta

print('*')
print('*')

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda
if len(texto_1)>len(texto_2):
    print('la primera palabra tiene más letras que la segunda: ', texto_1)
elif len(texto_1)==len(texto_2):
    print('ambas palabras ingresadas tienen la misma cantidad de letras')
else:
    print('la segunda palabra tiene más letras que la primera: ', texto_2)

print('*')
print('*')


# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

if texto_1[0]>texto_2[0]:
    print ('la primera letra de la primera palabra es mayor a la primera letra de la segunda palabra: ',texto_1[0])
elif texto_1[0]==texto_2[0]:
    print('ámbas palabras ingresadas comienzan con la misma letra: ', texto_1[0])
else:
    print ('la primera letra de la segunda palabra es mayor a la primera letra de la primera palabra: ',texto_2[0])
    

copia_texto_1 = texto_1  # Copia de la variable texto_1

print('*')
print('*')

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda
if copia_texto_1==texto_1:
    print('la copia de la primera palabra coincide con la misma')
else:
    print('la copia de la primera palabra no coincide con la ingresada por teclado')

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda
print('*')
print('fin del ejercicio')