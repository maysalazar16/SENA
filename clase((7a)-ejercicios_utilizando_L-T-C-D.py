'''escribe un programa que tenga dos listas y que, acontinuacion, cree las siguientes listas( en las que no debe haber repeticiones)

>Listas de los elementos que aparecen en las dos listas
>listas de elementos que aperecen en la primera lista, pero no en la segunda
>lista de elementos que aperecen en  la segunda lista , pero no en la primera
>liste de elementos que aparecen en ambas listas '''



# lista1 = [1,2,3,4,5,4,3,2,1,5]
# lista2 = [4,5,6,7,8,4,5,6,7,7,8]

# # elimiene los elementos que estan repetidos en las listas

# a = set(lista1)                         # esta forma convierto listas en conjuntos 
# b = set(lista2)

# union = list(a | b)             #elementos que aparecen en las dos listas          
# soloa = list(a - b)             # elementos que aperecen en la primera lista, pero no en la segunda
# solob = list( b - a)            # elementos que aperecen en  la segunda lista , pero no en la primera
# interseccion = list(a & b)      # elementos que aparecen en ambas listas 



# print(f"elementos que aparecen en las dos listas  {union}")
# print(f"elementos que aperecen en la primera lista, pero no en la segunda {soloa}")
# print(f"elementos que aperecen en  la segunda lista , pero no en la primera {solob}")
# print(f"elementos que aparecen en ambas listas {interseccion}")



# //////////////////////////////////////////////////////////////////////////////////////////////////////////

'''escriba un programa donde cree uana lista con los  siguientes peronajes del señor de los anillos 
nombre: aragorn
clase: guerrero
raza dunadan del norte

nombre: legolas
clase: arquero
raza: elfo sindar

nombre: candalf
clase: mago
raza: istar'''

# señor_de_los_anillos = {"Aragon":["guerra","dunada del norte"],"Legolas":["arquero","elfo sindar"],"Camdalf":["mago","istar"]}

# print(señor_de_los_anillos["Aragon"])
# print(señor_de_los_anillos["Legolas"])
# print(señor_de_los_anillos["Camdalf"])

# personaje = []                # crea la lista vacia 

# p = {"nombre":"Aragon","clase":"guerro","raza":"dunadan del norte"}
# personaje.append(p)              # agrega un disccionario a la lista 

# p = {"nombre":"Legolas","clase":"arquero","raza":"elfo sinda"}
# personaje.append(p)

# p = {"nombre":"Candal","clase":"mago","raza":"istar"}
# personaje.append(p)

# print(personaje)



'''***************************** ejercicios de listas y tuplas **********************************'''


'''escriba un programa que almanecene las asignaturas de un curso por ejemplo (matematicas, fisica, quimica, historia, religion )'''

# asignatura = ["matematicas","fisica","quimica","historia","religion"]

# print(asignatura)



'''escribe un programa que almacene las asignaturas de un curso por ejemplo (matematicas, fisica, quimica, historia, religion ) en una lista
y muestre por pantalla el mensaje "yo estudio <asignatura>, donde asignatura es cada una de las asignaturas de la lista "'''

# asignatura = ["matematicas","fisica","quimica","historia","religion"]

# for asignatura in asignatura:
#     print("yo estudio" + asignatura)

# 1. Crear y modificar una lista
numeros = [10, 20, 30, 40, 50]
numeros.append(60)  # Agregar un número
numeros[2] = 99  # Modificar el tercer elemento
del numeros[1]  # Eliminar el segundo elemento
print("Lista final:", numeros)

# 2. Recorrer una lista con 'for'
nombres = ["Ana", "Luis", "Carlos", "María"]
for nombre in nombres:
    print("Nombre:", nombre)

# 3. Encontrar el número mayor en una lista
numeros = [15, 8, 22, 31, 7]
mayor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num
print("El número mayor es:", mayor)

# 4. Sumar los elementos de una lista
numeros = [1, 2, 3, 4, 5]
suma = sum(numeros)
print("La suma de los números es:", suma)

# 5. Contar elementos en una lista
frutas = ["manzana", "pera", "manzana", "naranja", "pera", "manzana"]
conteo_manzanas = frutas.count("manzana")
print("Número de manzanas en la lista:", conteo_manzanas)

# 6. Convertir una lista en conjunto para eliminar duplicados
numeros_repetidos = [1, 2, 3, 1, 2, 4, 5]
numeros_unicos = list(set(numeros_repetidos))
print("Lista sin duplicados:", numeros_unicos)

# 7. Ordenar una lista de números
numeros = [3, 1, 4, 1, 5, 9, 2]
numeros.sort()
print("Lista ordenada:", numeros)

# 8. Invertir una lista
numeros.reverse()
print("Lista invertida:", numeros)

# 9. Crear una tupla e intentar modificarla
tupla = (10, 20, 30, 40, 50)
print("Tupla original:", tupla)
# tupla[1] = 99  # Esto generaría un error porque las tuplas son inmutables

# 10. Convertir una tupla en lista y modificarla
tupla = (1, 2, 3, 4, 5)
lista = list(tupla)
lista.append(6)
print("Lista modificada:", lista)

# 11. Acceder a elementos de una tupla
tupla = ("lunes", "martes", "miércoles", "jueves", "viernes")
print("Primer día de la semana:", tupla[0])
print("Último día de la semana:", tupla[-1])

# 12. Desempaquetar una tupla
tupla = ("rojo", "verde", "azul")
color1, color2, color3 = tupla
print("Colores desempaquetados:", color1, color2, color3)

# 13. Contar elementos en una tupla
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
conteo_cuatro = tupla.count(4)
print("Número de veces que aparece el 4:", conteo_cuatro)

# 14. Encontrar el índice de un elemento en una tupla
tupla = ("a", "b", "c", "d")
indice = tupla.index("c")
print("Índice de 'c':", indice)

# 15. Concatenar dos tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)





