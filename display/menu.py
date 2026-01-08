
def get_dyn_menu(header,options,exit,width,extras=[]):
    extraWidth = 0
    for parametro in extras:
        extraWidth += parametro[0]
    cabecera = "+" + "".center(width+extraWidth,"=") + "+\n" +\
               "|" + "".center(width+extraWidth," ") + "|\n" +\
               "|" + header.center(width+extraWidth," ") + "|\n" +\
               "|" + "".center(width+extraWidth," ") + "|\n" +\
               "|" + "".center(width+extraWidth,"-") + "|\n" +\
               "|" + "".center(width+extraWidth," ") + "|\n"
    opciones = ""
    # -----------------------------------------------------------------------------------------
    if not len(options):
        opciones += "|" + "   No hay opciones disponibles".ljust(width+extraWidth," ") + "|\n"
    else:
        for i in range(len(options)):
            opciones += "|" + ("   [{}]  {}".format(i+1,options[i])).ljust(width," ")
            if extras:
                parametros = "["
                for j in range(len(extras)):
                    parametro = extras[j]
                    if len(parametro) == 3:
                        parametros += parametro[2]
                    parametros += parametro[1][i]
                    if j == len(extras) - 1:
                        parametros += "]"
                    else:
                        parametros += " | "
                opciones += parametros.ljust(extraWidth," ")
            opciones += "|\n"
    opciones += "|" + "".center(width+extraWidth," ") + "|\n" +\
                "|" + ("   [0]  {}".format(exit)).ljust(width+extraWidth," ") + "|\n" +\
                "|" + "".center(width+extraWidth," ") + "|\n" +\
                "+" + "".center(width+extraWidth,"=") + "+\n\n"
    # -----------------------------------------------------------------------------------------

    while True:
        try:
            print(cabecera+opciones)
            opc = int(input("Selecciona una opción: "))

            if opc in range(0, len(options)+1):
                return opc
            else:
                print("Opción fuera del rango".center(width+2, "-"))
                input("Pulsa enter para continuar\n")

        except ValueError:
            print("Debes introducir un número entero".center(width+2, "-"))
            input("Pulsa enter para continuar\n")