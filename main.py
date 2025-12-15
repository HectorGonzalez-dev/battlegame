import utils.file_manager as fm
import display.menu as menu

menu_principal=("Bienvenido",("Nueva Partida","Cargar Partida","Editor"),"Salir")

salir = False
estado = "principal"

while not salir:

    while estado == "principal":
        opc = menu.get_menu(menu_principal[0],menu_principal[1],menu_principal[2])

        if opc == 1: # Nueva Partida
            estado = "nueva_partida"

        elif opc == 2: # Cargar Partida
            print()

        elif opc == 3: # Editor
            print()
        
        else: # Salir
            estado = ""
            salir = True
    
    while estado == "nueva_partida":
        