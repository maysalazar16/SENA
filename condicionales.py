# 1. Verifica si un número es positivo, negativo o cero.

numero1 = float(input("ingrese un numero: "))

if numero1 > 0:
    print(f"positivo porque es {numero1}")
elif numero1 < 0 :
    print(f"es negativo porque ese {numero1}")
else:
    print(f"es cero {numero1} ")
    
# 2. Calcula el mayor de dos números ingresados._
    
num1 = int(input("ingresar un numero"))
num2 = int(input("ingresar un numero"))

if num1 > num2:
    print("es mayor ")