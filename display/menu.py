
def get_menu(header,options,exit):
    cabecera = "+" + "".center(41,"=") + "+\n" +\
               "|" + "".center(41," ") + "|\n" +\
               "|" + header.center(41," ") + "|\n" +\
               "|" + "".center(41," ") + "|\n" +\
               "|" + "".center(41,"-") + "|\n" +\
               "|" + "".center(41," ") + "|\n"
    opciones = ""
    if not len(options):
        opciones += "|" + "   No hay opciones disponibles".ljust(41," ") + "|\n"
    else:
        for i in range(len(options)):
            opciones += "|" + ("   [{}]  {}".format(i+1,options[i])).ljust(41," ") + "|\n"
    opciones += "|" + "".center(41," ") + "|\n" +\
                "|" + ("   [0]  {}".format(exit)).ljust(41," ") + "|\n" +\
                "|" + "".center(41," ") + "|\n" +\
                "+" + "".center(41,"=") + "+\n\n"

    while True:
        try:
            print(cabecera+opciones)
            opc = int(input("Selecciona una opción: "))

            if opc in range(0, len(options)+1):
                return opc
            else:
                print("Opción fuera del rango".center(43, "-"))
                input("Pulsa enter para continuar\n")

        except ValueError:
            print("Debes introducir un número entero".center(43, "-"))
            input("Pulsa enter para continuar\n")

def set_name():
    while True:
        try:
            nombre = input("Nombre del pj (20 caracteres max): ").strip()
            nombre_solo_letras = nombre.replace(" ","")
            if nombre.count("  ") == 0 and len(nombre) <= 20 and nombre_solo_letras.isalpha() == True:
                return nombre
            else:
                if nombre.count("  ") > 0:
                    print("El nombre no puede tener 2 espacios seguidos")
                if len(nombre) > 20:
                    print("El nombre es demasiado largo")
                if nombre_solo_letras.isalpha() == False:
                    print("El nombre solo puede contener letras")
