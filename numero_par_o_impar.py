'''***************************** istema de numeros pares he impares **********************************'''

'''se solicita crea un programa que indique si un numero es ar o impar\n'''

print("sistema de numeros pares he impares")
# num = int(input("digite un numero: "))

# if num %2==0:
#     print("el numero es par")
# else:
#     print("el numero es impar:")

'''***************************** istema de dos numeros pares he impares **********************************'''

# num = int(input("digite un numero: "))
# num1 = int(input("digite otro numero: "))

# result = num / num1 

# if result %2==0:
#     print(f"el resultado es {result} y cuenta coomo un numeoro PAR")
# else:
#     print(f"el resultado es {result} y cuenta como un numero IMPAR")


# Números Pares e Impares en Python
# Un número es par si es divisible por 2 sin dejar residuo (n % 2 == 0)
# Un número es impar si deja residuo al dividirlo por 2 (n % 2 != 0)

# 1. Verificar si un número es par o impar
# numero = 7
# if numero % 2 == 0:
#     print(f"{numero} es par")
# else:
#     print(f"{numero} es impar")

# # 2. Generar una lista de números pares del 1 al 20
# pares = [n for n in range(1, 21) if n % 2 == 0]
# print("Números pares:", pares)

# # 3. Generar una lista de números impares del 1 al 20
# impares = [n for n in range(1, 21) if n % 2 != 0]
# print("Números impares:", impares)

# # 4. Contar cuántos números pares hay en una lista
# datos = [3, 8, 15, 22, 7, 10, 18]
# cantidad_pares = sum(1 for n in datos if n % 2 == 0)
# print("Cantidad de pares en la lista:", cantidad_pares)

# # 5. Contar cuántos números impares hay en una lista
# cantidad_impares = sum(1 for n in datos if n % 2 != 0)
# print("Cantidad de impares en la lista:", cantidad_impares)

# # 6. Imprimir los primeros 10 números pares
# for i in range(2, 21, 2):
#     print(i, end=" ")
# print()

# # 7. Imprimir los primeros 10 números impares
# for i in range(1, 20, 2):
#     print(i, end=" ")
# print()

# # 8. Filtrar los números pares de una lista
# datos = [4, 7, 12, 15, 20, 33]
# numeros_pares = list(filter(lambda x: x % 2 == 0, datos))
# print("Números pares filtrados:", numeros_pares)

# # 9. Filtrar los números impares de una lista
# numeros_impares = list(filter(lambda x: x % 2 != 0, datos))
# print("Números impares filtrados:", numeros_impares)

# # 10. Sumar los números pares de una lista
# suma_pares = sum(n for n in datos if n % 2 == 0)
# print("Suma de los números pares:", suma_pares)

# # 11. Sumar los números impares de una lista
# suma_impares = sum(n for n in datos if n % 2 != 0)
# print("Suma de los números impares:", suma_impares)

# # 12. Determinar si un número ingresado por el usuario es par o impar
# num_usuario = int(input("Ingrese un número: "))
# if num_usuario % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")

# # 13. Generar una tupla con números pares hasta 50
# tupla_pares = tuple(n for n in range(2, 51, 2))
# print("Tupla de pares:", tupla_pares)

# # 14. Generar una tupla con números impares hasta 50
# tupla_impares = tuple(n for n in range(1, 50, 2))
# print("Tupla de impares:", tupla_impares)

# # 15. Encontrar el número par más grande en una lista
# datos = [11, 22, 35, 40, 52, 63]
# max_par = max((n for n in datos if n % 2 == 0), default=None)
# print("Número par más grande:", max_par)

# # 16. Encontrar el número impar más pequeño en una lista
# min_impar = min((n for n in datos if n % 2 != 0), default=None)
# print("Número impar más pequeño:", min_impar)

# # 17. Separar pares e impares en dos listas diferentes
# datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares_lista, impares_lista = [], []
# for n in datos:
#     if n % 2 == 0:
#         pares_lista.append(n)
#     else:
#         impares_lista.append(n)
# print("Lista de pares:", pares_lista)
# print("Lista de impares:", impares_lista)

# # 18. Crear un diccionario con números y su clasificación (par o impar)
# numeros_dict = {n: "par" if n % 2 == 0 else "impar" for n in range(1, 21)}
# print("Diccionario de números:", numeros_dict)

# # 19. Verificar si todos los números en una lista son pares
# datos = [2, 4, 6, 8, 10]
# es_todo_par = all(n % 2 == 0 for n in datos)
# print("¿Todos los números son pares?", es_todo_par)

# # 20. Verificar si hay al menos un número impar en la lista
# hay_impar = any(n % 2 != 0 for n in datos)
# print("¿Hay algún número impar?", hay_impar)
