# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
print('*')
if texto_1>texto_2:
    print('el primer texto es mayor que el segundo: ', texto_1)
elif texto_1==texto_2:
    print('ambos textos son iguales')
else:
    print('el segundo texto es mayor que el primero: ', texto_2)
    
print('*')

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
num_1=int(texto_1)
num_2=int(texto_2)
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
if num_1>num_2:
    print('el primer numero es mayor que el segundo: ', num_1)
elif num_1==num_2:
    print('ambos números son iguales')
else:
    print('el segundo número es mayor que el primero: ', num_2)
    
print('*')
# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
print('RESPUESTA: porque el código ASCII del símbolo 7 es mayor que el del símbolo 5')
print('*')
print('FIN DEL EJERCICIO')
