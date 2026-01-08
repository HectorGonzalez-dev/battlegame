import utils.file_manager as fm
import display.menu as menu

menu_principal=("Perdido en el terminal",("Nueva Partida","Cargar Partida","Editor"),"Salir")
menu_cargar_partida = ("Cargar Partida",None,"Volver")

salir = False
estado = "principal"

while not salir:

    while estado == "principal":
        opc = menu.get_menu(menu_principal[0],menu_principal[1],menu_principal[2])

        if opc == 1: # Nueva Partida
            print()

        elif opc == 2: # Cargar Partida
            estado = "cargar_partida"

        elif opc == 3: # Editor
            print()
        
        else: # Salir
            estado = ""
            salir = True

    while estado == "cargar_partida":
        saves = fm.get_data("data/saves.json")
        characters = fm.get_data("data/characters.json")
        savesKeys = list(saves.keys())
        nombres = []
        for key in savesKeys:
            nombres.append(characters[saves[key]["character"]]["name"])
        opc = menu.get_dyn_menu(menu_cargar_partida[0],savesKeys,menu_cargar_partida[2],20,[[20,nombres]])