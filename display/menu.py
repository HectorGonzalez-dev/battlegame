
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