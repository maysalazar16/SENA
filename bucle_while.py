"""El Bucle while en Python
El bucle while es una estructura de control que permite ejecutar repetidamente un bloque de código mientras se cumpla una condición determinada. A diferencia del bucle for, que itera sobre una secuencia de elementos,
el while se basa en una condición lógica que debe evaluarse como True para que el bucle continúe ejecutándose.


Sintaxis básica

while condición:
    # Código que se ejecuta mientras la condición sea True


La condición se evalúa antes de cada iteración. Si es False, el bucle se detiene y la ejecución continúa con el resto del programa.
Ejemplo básico
contador = 1
while contador <= 5:  
    print("Iteración:", contador)  
    contador += 1  # Incremento para evitar un bucle infinito
    

Manejo de bucles while
Uso de break para salir del bucle
Se puede usar la palabra clave break para terminar el bucle antes de que la condición sea falsa.

contador = 1
while contador <= 10:
    if contador == 5:
        print("Se detiene en:", contador)
        break  # Sale del bucle
    print("Número:", contador)
    contador += 1


Bucle while con else
Al igual que for, un while puede tener una cláusula else, que se ejecuta cuando la condición del while se vuelve False sin haber usado break.

contador = 1
while contador <= 3:
    print("Intento", contador)
    contador += 1
else:
    print("Bucle completado sin interrupciones")
    

Cuándo usar while en lugar de for
Se recomienda usar while cuando:
✔️ No se conoce de antemano cuántas veces se debe ejecutar el bucle.
✔️ Se necesita un bucle basado en una condición lógica en lugar de recorrer una secuencia.

Por ejemplo, para esperar una entrada de usuario válida:

entrada = ""
while entrada.lower() != "ok":
    entrada = input("Escribe 'ok' para continuar: ")
print("Gracias, continuamos...")"""

#bucle while

# import math


# numero  = int(input("Digite un numero: "))

# while numero < 0 :
#     print("Error -> deberia ser un numero positivio")
#     numero  = int(input("Digite un numero: "))

# print(f"\nSu raiz cuadrada es : {(math.sqrt(numero)):.2f}")


# # Ejemplo 1: Bucle while básico
# contador = 0
# while contador < 5:
#     print("Contador:", contador)
#     contador += 1

# # Ejemplo 2: Usar break para salir del bucle
# contador = 0
# while contador < 10:
#     if contador == 5:
#         print("Se encontró el 5, saliendo del bucle")
#         break
#     print("Contador:", contador)
#     contador += 1

# # Ejemplo 3: Usar continue para saltar una iteración
# contador = 0
# while contador < 5:
#     contador += 1
#     if contador == 3:
#         continue
#     print("Número procesado:", contador)

# # Ejemplo 4: Bucle infinito con condición de salida
# contador = 0
# while True:
#     print("Iteración:", contador)
#     contador += 1
#     if contador == 3:
#         break

# # Ejemplo 5: Contar hacia atrás
# contador = 5
# while contador > 0:
#     print("Cuenta regresiva:", contador)
#     contador -= 1

# # Ejemplo 6: Usar else en un bucle while
# contador = 0
# while contador < 3:
#     print("Intento", contador)
#     contador += 1
# else:
#     print("Bucle completado sin interrupciones")

# # Ejemplo 7: Leer entrada del usuario hasta que ingrese "salir"
# while True:
#     entrada = input("Escribe algo (o 'salir' para terminar): ")
#     if entrada.lower() == "salir":
#         break
#     print("Ingresaste:", entrada)

# # Ejemplo 8: Sumar números hasta alcanzar un límite
# suma = 0
# numero = 1
# while suma < 10:
#     suma += numero
#     print("Suma parcial:", suma)
#     numero += 1

# # Ejemplo 9: Usar while para validar una entrada numérica
# while True:
#     entrada = input("Ingresa un número positivo: ")
#     if entrada.isdigit() and int(entrada) > 0:
#         print("Número válido ingresado")
#         break
#     print("Entrada inválida, intenta de nuevo")

# # Ejemplo 10: Simular una cuenta bancaria
# saldo = 1000
# while saldo > 0:
#     retiro = int(input("Ingresa cantidad a retirar: "))
#     if retiro > saldo:
#         print("Fondos insuficientes")
#         continue
#     saldo -= retiro
#     print("Saldo restante:", saldo)
#     if saldo == 0:
#         print("Cuenta vacía")
#         break

# # Ejemplo 11: Usar while con listas
# lista = [1, 2, 3, 4, 5]
# while lista:
#     print("Elemento eliminado:", lista.pop())

# # Ejemplo 12: Generar números aleatorios hasta cumplir una condición
# import random
# numero = 0
# while numero != 7:
#     numero = random.randint(1, 10)
#     print("Número generado:", numero)

# # Ejemplo 13: Simulación de intentos de acceso
# intentos = 3
# while intentos > 0:
#     password = input("Ingresa la contraseña: ")
#     if password == "secreto":
#         print("Acceso concedido")
#         break
#     intentos -= 1
#     print("Intentos restantes:", intentos)
# else:
#     print("Acceso denegado")

# # Ejemplo 14: Generar secuencia de Fibonacci
# num1, num2 = 0, 1
# contador = 0
# while contador < 10:
#     print(num1)
#     num1, num2 = num2, num1 + num2
#     contador += 1

# # Ejemplo 15: Imprimir números impares menores a 10
# numero = 1
# while numero < 10:
#     print("Número impar:", numero)
#     numero += 2

# # Ejemplo 16: Bucle con decremento controlado
# valor = 20
# while valor >= 0:
#     print("Valor actual:", valor)
#     valor -= 4

# # Ejemplo 17: Multiplicación acumulativa
# producto = 1
# numero = 1
# while numero <= 5:
#     producto *= numero
#     print("Producto parcial:", producto)
#     numero += 1

# # Ejemplo 18: Simulación de lanzamiento de dados
# import random
# dado = 0
# while dado != 6:
#     dado = random.randint(1, 6)
#     print("Dado lanzado, salió:", dado)

# # Ejemplo 19: Contador de vocales en una palabra
# palabra = "programacion"
# indice = 0
# vocales = "aeiou"
# contador_vocales = 0
# while indice < len(palabra):
#     if palabra[indice] in vocales:
#         contador_vocales += 1
#     indice += 1
# print("Cantidad de vocales:", contador_vocales)

# # Ejemplo 20: Contador de dígitos en un número
# numero = 123456
# contador = 0
# while numero > 0:
#     numero //= 10
#     contador += 1
# print("Cantidad de dígitos:", contador)

# # Ejemplo 21: Invertir una cadena con while
# cadena = "Python"
# invertida = ""
# indice = len(cadena) - 1
# while indice >= 0:
#     invertida += cadena[indice]
#     indice -= 1
# print("Cadena invertida:", invertida)

# # Ejemplo 22: Contador de palabras en una frase
# frase = "El lenguaje de programación Python es genial"
# palabras = frase.split()
# contador = 0
# while contador < len(palabras):
#     print("Palabra:", palabras[contador])
#     contador += 1

# # Ejemplo 23: Contador de números pares hasta 20
# contador = 0
# numero = 0
# while numero <= 20:
#     if numero % 2 == 0:
#         contador += 1
#     numero += 1
# print("Cantidad de números pares:", contador)

# # Ejemplo 24: Suma de números hasta alcanzar un valor dado
# suma = 0
# numero = 1
# while suma < 50:
#     suma += numero
#     print("Suma parcial:", suma)
#     numero += 1

# # Ejemplo 25: Bucle anidado con while
# x = 1
# while x <= 3:
#     y = 1
#     while y <= 3:
#         print(f"x={x}, y={y}")
#         y += 1
#     x += 1


"""Conclusión
El bucle while es una herramienta poderosa para repetir tareas mientras una condición se mantenga True. Su correcta implementación puede hacer que los programas sean más dinámicos y eficientes,
pero es importante evitar bucles infinitos y manejar correctamente las salidas con break o continue cuando sea necesario."""