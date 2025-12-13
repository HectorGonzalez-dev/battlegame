
def display_menu(header,options,exit):
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
    print(cabecera+opciones)