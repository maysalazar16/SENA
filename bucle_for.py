'''bucle FOR son estructuras de codigo que cambian la ejecucion


esta recomentdo para contexti en los que se sabe el numero de iteracione que se van a dar en su ejecucion, es decir, es un bucle que busca ejecutar
un conjunto de instrucciones de forma repetitiva hasta llegar al numero maximo de iteraciones definidas

en python los bucles for se ejecutan sobre elementos iterables, como puden ser listas, tuplas, cadenas de texto, o dicionarios. El numero de teraciones
que se ejecutaran dependera del numero de los elementos de los que esta compiesto el elemento iterable

los bucles for tienen la siguiente sintaxis


for variable in coleccoomIterable:
    .        BloqueInstrucines
    
for: indica el comienzo de un bucle
variabel: vriable que almacena el elemento sobre el que se esta iterand de coleccioniterable
in: indicador wur se utilizs psra definir el elemento itrrable sobre el que se ejecutara el bucle for
ColeccionIterable: elemento sobre el que se ejecuta el bucle
BloqueIstrucciones: conjunto de intrucciones que se ejecuraran en cada cadena 



paso a paso del bucle for en Python:
Definir una lista: Se crea una lista llamada numeros con los valores [1, 2, 3, 4, 5].

Iniciar el bucle for: Se utiliza for numero in numeros: para recorrer cada elemento de la lista.

Ejecutar el bloque de código: Dentro del bucle, print("El número es:", numero) se ejecuta en cada iteración, mostrando el valor actual de numero.p'''




#ejemplo


# lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
# for lista in lista :
#     print(lista, end=" ")



# for x in range(0,5):  #range para pango de numero
#     print("hola el numero de X es ", x)

for x in "hola":
    print(x)
#lista

# nombre = ["juan","pedro","elena"]
# print("el tipo de nombre es", type(nombre))     # type indica que tipo es si es tipo lista tipo diccionario
# for nombre in nombre:
#     print("Buenos dias", nombre)

#Tuple

# nombre =("juan", "ana", "elena")
# print("el tipo de nomnre es", type(nombre))
# for nombre in nombre:
#     print("buenos dias ", nombre)


# set    el metodo set altera el orden al momento de imprimir el resultado 

# nombre = {"juan", "ana","elena"}
# print("el tipo de nombre es ", type(nombre))
# for nombre in nombre:
#     print("Buenos dias", nombre)


#Diccionario
# nombre = {"juan" : 1, "ana" : 2, "elena" : 3}
# print("el tipo de nombre es ", type(nombre))
# for nombre in nombre:
#     print("buenos dias", nombre)

# Ejemplo 1: Recorrer una lista de números
# numeros = [1, 2, 3, 4, 5]
# for numero in numeros:
#     print("El número es:", numero)

# # Ejemplo 2: Recorrer una cadena de texto
# texto = "Python"
# for letra in texto:
#     print("Letra:", letra)

# # Ejemplo 3: Usar range() para generar una secuencia de números
# for i in range(5):
#     print("Iteración:", i)

# # Ejemplo 4: Recorrer una lista de nombres
# nombres = ["Ana", "Juan", "Carlos"]
# for nombre in nombres:
#     print("Hola", nombre)

# # Ejemplo 5: Usar un bucle for con una tupla
# colores = ("rojo", "verde", "azul")
# for color in colores:
#     print("Color:", color)

# # Ejemplo 6: Iterar sobre un diccionario
# diccionario = {"a": 1, "b": 2, "c": 3}
# for clave, valor in diccionario.items():
#     print("Clave:", clave, "Valor:", valor)

# # Ejemplo 7: Usar break para salir del bucle
# tareas = ["cocinar", "limpiar", "estudiar"]
# for tarea in tareas:
#     if tarea == "limpiar":
#         print("Tarea encontrada, saliendo del bucle.")
#         break
#     print("Tarea pendiente:", tarea)

# # Ejemplo 8: Usar continue para saltar una iteración
# for numero in range(1, 6):
#     if numero == 3:
#         continue
#     print("Número procesado:", numero)

# # Ejemplo 9: Usar else con un bucle for
# for i in range(3):
#     print("Intento", i)
# else:
#     print("Bucle completado sin interrupciones")

# # Ejemplo 10: Usar for con enumerate
# frutas = ["manzana", "banana", "cereza"]
# for indice, fruta in enumerate(frutas):
#     print(f"Índice {indice}: {fruta}")

# # Ejemplo 11: Iterar sobre una lista de listas
# matriz = [[1, 2], [3, 4], [5, 6]]
# for fila in matriz:
#     for elemento in fila:
#         print("Elemento:", elemento)

# # Ejemplo 12: Iterar sobre un conjunto
# conjunto = {"perro", "gato", "loro"}
# for animal in conjunto:
#     print("Animal:", animal)

# # Ejemplo 13: Iterar con zip para recorrer dos listas simultáneamente
# nombres = ["Ana", "Juan", "Carlos"]
# edades = [25, 30, 22]
# for nombre, edad in zip(nombres, edades):
#     print(f"{nombre} tiene {edad} años")

# # Ejemplo 14: Iterar de forma inversa con reversed()
# numeros = [1, 2, 3, 4, 5]
# for numero in reversed(numeros):
#     print("Número en orden inverso:", numero)

# # Ejemplo 15: Iterar con range con paso diferente
# for i in range(0, 10, 2):
#     print("Número con paso 2:", i)

# # Ejemplo 16: Iterar sobre caracteres de una palabra sin repetir
# palabra = "banana"
# for letra in set(palabra):
#     print("Letra única:", letra)

# # Ejemplo 17: Generar una lista con comprensión de listas
# cuadrados = [x**2 for x in range(10)]
# print("Lista de cuadrados:", cuadrados)

# # Ejemplo 18: Filtrar elementos con comprensión de listas
# pares = [x for x in range(20) if x % 2 == 0]
# print("Números pares:", pares)

# # Ejemplo 19: Iterar sobre caracteres ASCII
# for i in range(65, 91):
#     print("Letra:", chr(i))

# # Ejemplo 20: Usar for para contar ocurrencias en una lista
# colores = ["rojo", "azul", "verde", "rojo", "azul"]
# conteo = {}
# for color in colores:
#     conteo[color] = conteo.get(color, 0) + 1
# print("Conteo de colores:", conteo)

# # Ejemplo 21: Iterar sobre una lista con un índice manual
# lista = ["a", "b", "c", "d"]
# indice = 0
# for elemento in lista:
#     print(f"Índice {indice}: {elemento}")
#     indice += 1

# # Ejemplo 22: Iterar sobre una lista en orden descendente
# numeros = [5, 3, 8, 1]
# for numero in sorted(numeros, reverse=True):
#     print("Número ordenado desc:", numero)

# # Ejemplo 23: Iterar y modificar elementos de una lista
# numeros = [1, 2, 3, 4, 5]
# numeros = [x * 2 for x in numeros]
# print("Lista duplicada:", numeros)

# # Ejemplo 24: Iterar con while dentro de un for
# for i in range(5):
#     while i < 3:
#         print("Valor de i dentro del while:", i)
#         i += 1

# # Ejemplo 25: Usar itertools para generar combinaciones
# from itertools import permutations
# letras = ["a", "b", "c"]
# for perm in permutations(letras):
#     print("Permutación:", perm)
