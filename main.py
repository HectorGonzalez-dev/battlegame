import utils.file_manager as fileman
import display.menu as menu
import utils.list_manager as listman

menu_principal=("Perdido en el terminal",("Nueva Partida","Cargar Partida","Editor"),"Salir")
menu_cargar_partida = ("Cargar Partida",None,"Volver")

salir = False
estado = "principal"

while not salir:

    while estado == "principal":
        opc = menu.get_dyn_menu(menu_principal[0],menu_principal[1],menu_principal[2],40)

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
        saves = fileman.get_data("data/saves.json")
        characters = fileman.get_data("data/characters.json")
        savesKeys = listman.bubble_sort(list(saves.keys()))
        print(savesKeys)
        nombres = []
        for key in savesKeys:
            nombres.append(characters[saves[key]["character"]]["name"])
        opc = menu.get_dyn_menu(menu_cargar_partida[0],savesKeys,menu_cargar_partida[2],20,[[20,nombres]])