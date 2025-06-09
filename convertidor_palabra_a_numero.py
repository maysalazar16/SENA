print("convertidor de palabrass\n")

print("MENU DE OPCIONES")

print("presione 1 para convertir de numero a palabra \npresione 2 para convertir de palabra a numero")

opc = int(input("¿cual es tu opcion deseada?: "))

if opc == 1:
    print("conversor de numero a palabra")
    num =int(input("cual es el numero que deseas convertir a palabra: "))#######
    if num == 1:
        print("uno")
    elif num == 2:
        print("dos")
    elif num == 3:
        print("tres")
    elif num == 4:
        print("cuatro")
    elif num == 5:
        print("cinco")
    elif num == 6:
        print("seis")
    elif num == 7:
        print("sitete")
    else:
        print("onumero no registrado ")
 
elif opc == 2:
    print("conversor de palabra a numero\n")
    num1 = input("cual es la palabra que deseas convertir a numero: ")
    if num1 == ("uno"):
        print("1")
    elif num1 ==("dos"):
        print("dos")
    elif num1 ==("tres"):
        print("3")
    elif num1 ==("cuatro"):
        print("4")
    elif num1 ==("cinco"):
        print("5")
    elif num1 ==("seis"):
        print("6")
    elif num1 ==("siete"):
        print("7")
    else:
        print("palabra nor registrada: ")
else:
    
    print("opcion no disponible: ")


