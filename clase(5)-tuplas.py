'''las TUPLAS son simplemente otro tipo de coleccion que realmente son muy parecidos a las listas, pero con la gran diferencia que las TUPLAS son listas inmutabes
a que me refiero con esto, sencillamente a que no vamos a poder modificsrlas, es decir no vamos a poder añadir nuevos elementos,
no vamos a poder eliminar elementos de las tuplas, ni tampoco modificar los elemento que ya tenemos  

recordar que  las tuplas van en parentesis ()'''

'''son mucho mas rapidas a sus momentos de ejecucion y pues consumen mucho menos memoria que las listas '''


'''          ***NO PODEMOS HACER***                                                             ***SI PODEMOS HACER*** 
.append() = agrega elementos al final de la lista                            print(tupla[1]) = podemos mostrar lo que hay en cada indice
lista[0] = 8  = nos modifica el valor de indice                              print(tupla[1:]) = que nos muestre todos los elemento desde la posicion 1 en adelante
tupla.pop() eliminar un indice de una tupla                                  print(4 in tupla) = busca si el valor de 4 esta en nuestra tupla
tupla.pop() eliminar                                                        .index(()) = indica el indice donde esta dicho elemento ***print(tupla.index(5))***                            
.                                                                           .count(()) = indica cuantas veces esta repetido un valor en la tupla ***print(tupla.count("salazar"))***
.                                                                            list(tupla) combierte nuestra Tupla en una lista '''




# tupla = (4,"hola",6.78,[1,2,3],4) # esto es una tupla

# print(tupla[-1])
# print(tupla[1:])
# print(4 in tupla)
# print(tupla.index(6.78))
# print(tupla.count(6))

'''tambien podemos transformar listas en tuplas y tuplas en listas '''

# tupla = (4,"hola",6.78,[1,2,3],4)
# lista= list(tupla)                  #la funcion list tranformara nuestra tupla en una lista 

# print(lista)

# ¿Qué es una tupla?
# Una tupla es una estructura de datos en Python similar a una lista,
# pero con la diferencia de que es inmutable, es decir, no se puede modificar después de su creación.

# 1. Crear una tupla
# mi_tupla = (1, 2, 3, 4, 5)
# print("Tupla:", mi_tupla)

# # 2. Acceder a elementos de una tupla
# print("Primer elemento:", mi_tupla[0])
# print("Último elemento:", mi_tupla[-1])

# # 3. Intentar modificar una tupla (esto dará error)
# # mi_tupla[1] = 10  # Error, las tuplas son inmutables

# # 4. Desempaquetar una tupla
# (a, b, c, d, e) = mi_tupla
# print("Valores desempaquetados:", a, b, c, d, e)

# # 5. Concatenar dos tuplas
# tupla1 = (1, 2, 3)
# tupla2 = (4, 5, 6)
# tupla_concatenada = tupla1 + tupla2
# print("Tupla concatenada:", tupla_concatenada)

# # 6. Repetir una tupla
# tupla_repetida = tupla1 * 3
# print("Tupla repetida:", tupla_repetida)

# # 7. Verificar si un elemento está en una tupla
# print(3 in mi_tupla)  # True
# print(10 in mi_tupla)  # False

# # 8. Obtener la longitud de una tupla
# print("Longitud de la tupla:", len(mi_tupla))

# # 9. Contar elementos en una tupla
# tupla_contar = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
# print("Número de veces que aparece el 3:", tupla_contar.count(3))

# # 10. Encontrar el índice de un elemento
# tupla_indices = ("a", "b", "c", "d")
# print("Índice de 'c':", tupla_indices.index("c"))

# # 11. Convertir una tupla en lista
# lista_desde_tupla = list(mi_tupla)
# print("Lista desde tupla:", lista_desde_tupla)

# # 12. Convertir una lista en tupla
# lista = [10, 20, 30]
# tupla_desde_lista = tuple(lista)
# print("Tupla desde lista:", tupla_desde_lista)

# # 13. Crear una tupla con un solo elemento
# una_tupla = (5,)
# print("Tupla con un solo elemento:", una_tupla)

# # 14. Iterar sobre una tupla
# tupla_iterar = ("rojo", "verde", "azul")
# for color in tupla_iterar:
#     print("Color:", color)

# # 15. Usar `max()` y `min()` en tuplas numéricas
# tupla_numerica = (10, 20, 5, 30, 25)
# print("Máximo:", max(tupla_numerica))
# print("Mínimo:", min(tupla_numerica))

# # 16. Crear una tupla anidada
# tupla_anidada = ((1, 2), (3, 4), (5, 6))
# print("Tupla anidada:", tupla_anidada)

# # 17. Acceder a elementos de una tupla anidada
# print("Elemento (1,2):", tupla_anidada[0])
# print("Elemento 3:", tupla_anidada[1][0])

# # 18. Comparar tuplas
# tupla_a = (1, 2, 3)
# tupla_b = (1, 2, 4)
# print("¿Son iguales?:", tupla_a == tupla_b)
# print("¿Es menor?:", tupla_a < tupla_b)

# # 19. Usar tuplas en funciones
# def coordenadas():
#     return (10.5, 20.3)

# x, y = coordenadas()
# print("Coordenadas:", x, y)

# # 20. Convertir una cadena en tupla
# cadena = "Python"
# tupla_desde_cadena = tuple(cadena)
# print("Tupla desde cadena:", tupla_desde_cadena)




''''''