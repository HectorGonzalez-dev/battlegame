def nuevo_nombre():
    nombre = input("Nombre del pj (20 caracteres max): ").strip()
    nombre_solo_letras = nombre.replace(" ","")
    if nombre.count("  ") == 0 and len(nombre) <= 20 and nombre_solo_letras.isalpha() == True:
        print("Nombre aceptado")
        return nombre
    else:
        if nombre.count("  ") > 0:
            print("El nombre no puede tener 2 espacios seguidos")
        if len(nombre) > 20:
            print("El nombre es demasiado largo")
        if nombre_solo_letras.isalpha() == False:
            print("El nombre solo puede contener letras")
        print("Nombre rechazado")
        input("Enter para volver")
        return ""

def tipo_energia():
    energias = ("Maná","Stamina")
    while True:
        try:
            print("[1] "+energias[0]+"\n"+"[2] "+energias[1])
            opc = int(input("Elige tu tipo de energía: "))
            if opc in range(1,3):
                if opc == 1:
                    energia = energias[0]
                else:
                    energia = energias[1]
                return energia
            else:
                print("Opción fuera del rango")
                input("Pulsa enter para continuar\n")
        except ValueError:
            print("Debes introducir un número entero")
            input("Pulsa enter para continuar\n")