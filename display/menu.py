
def get_menu(header,options,exit,width,extras=[]):
    extraWidth = 0
    if extras:
        extraWidth = extras[0]
    cabecera = "+" + "".center(width+extraWidth,"=") + "+\n" +\
               "|" + "".center(width+extraWidth," ") + "|\n" +\
               "|" + header.center(width+extraWidth," ") + "|\n" +\
               "|" + "".center(width+extraWidth," ") + "|\n" +\
               "|" + "".center(width+extraWidth,"-") + "|\n" +\
               "|" + "".center(width+extraWidth," ") + "|\n"
    opciones = ""

    if not len(options):
        opciones += "|" + "   No hay opciones disponibles".ljust(width+extraWidth," ") + "|\n"
    else:
        for i in range(len(options)):
            opciones += "|" + ("   [{}]  {}".format(i+1,options[i])).ljust(width," ")
            if extras:
                parametros = ""
                for j in range(1,len(extras)):
                    parametro = extras[j]
                    if parametro[0] == i+1:
                        parametros = "["
                        for k in range(1,len(parametro)):
                            if type(parametro[k]) == str:
                                parametros += parametro[k]
                            else:
                                parametros += parametro[k][1] + parametro[k][0]
                            if k != len(parametro)-1:
                                parametros += " | "
                            else:
                                parametros += "]"
                opciones += parametros.ljust(extraWidth," ")
            opciones += "|\n"
    opciones += "|" + "".center(width+extraWidth," ") + "|\n" +\
                "|" + ("   [0]  {}".format(exit)).ljust(width+extraWidth," ") + "|\n" +\
                "|" + "".center(width+extraWidth," ") + "|\n" +\
                "+" + "".center(width+extraWidth,"=") + "+\n"

    while True:
        try:
            print(cabecera+opciones)
            opc = int(input("Selecciona una opción: "))

            if opc in range(0, len(options)+1):
                return opc
            else:
                print("Opción fuera del rango".center(width+2+extraWidth, "-"))
                input("Pulsa enter para continuar\n")

        except ValueError:
            print("Debes introducir un número entero".center(width+2+extraWidth, "-"))
            input("Pulsa enter para continuar\n")

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
                "+" + "".center(width+extraWidth,"=") + "+\n"

    while True:
        try:
            print(cabecera+opciones)
            opc = int(input("Selecciona una opción: "))

            if opc in range(0, len(options)+1):
                return opc
            else:
                print("Opción fuera del rango".center(width+2+extraWidth, "-"))
                input("Pulsa enter para continuar\n")

        except ValueError:
            print("Debes introducir un número entero".center(width+2+extraWidth, "-"))
            input("Pulsa enter para continuar\n")

def display_battle_menu(current_enemies,current_player,option_list):
    width = 50
    cabecera = "+" + "".center(width,"=") + "+\n" +\
               "|" + "".center(width," ") + "|\n" +\
               "|" + "BATALLA EN CURSO".center(width," ") + "|\n" +\
               "|" + "".center(width," ") + "|\n" +\
               "|" + "".center(width,"-") + "|\n" +\
               "|" + "".center(width," ") + "|\n"
    cuerpo = "|" + "   Enemigos:".ljust(width," ") + "|\n"
    for enemy in current_enemies:
        cuerpo += "|" + ("   {} [Vida: {}/{}]".format(enemy["name"],enemy["current_health"],enemy["health"])).ljust(width," ") + "|\n"
    cuerpo += "|" + "".center(width," ") + "|\n" +\
              "|" + "   Jugador:".ljust(width," ") + "|\n" +\
              "|" + ("   {} [Vida: {}/{}]".format(current_player["name"],current_player["current_health"],current_player["health"])).ljust(width," ") + "|\n" +\
              "|" + "".center(width," ") + "|\n" +\
              "|" + "".center(width,"-") + "|\n"
    opciones = "|" + "".center(width," ") + "|\n"
    for i in range(len(option_list)):
        opciones += "|" + ("   [{}]  {}".format(i+1,option_list[i])).ljust(width," ") + "|\n"
    opciones += "|" + "".center(width," ") + "|\n" + "+" + "".center(width,"=") + "+\n"

    while True:
        try:
            print(cabecera+cuerpo+opciones)
            opc = int(input("Selecciona una opción: "))

            if opc in range(0, len(option_list)+1):
                return opc
            else:
                print("Opción fuera del rango".center(width+2, "-"))
                input("Pulsa enter para continuar\n")

        except ValueError:
            print("Debes introducir un número entero".center(width+2, "-"))
            input("Pulsa enter para continuar\n")
