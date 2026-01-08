import utils.file_manager as fileman
import display.menu as menu
import utils.list_manager as listman
import utils.char_manager as char_manager

menu_principal=("Perdido en el terminal",("Nueva Partida","Cargar Partida","Editor"),"Salir")
menu_cargar_partida = ("Cargar Partida",None,"Volver")
menu_nueva_partida = ("Nueva Partida",("Nombre","Estadísticas","Tipo de energía","Confirmar"),"Volver")

salir = False
estado = "principal"
nombre = ""
energia = ""

while not salir:

    while estado == "principal":
        opc = menu.get_menu(menu_principal[0],menu_principal[1],menu_principal[2],40)

        if opc == 1: # Nueva Partida
            estado = "nueva_partida"

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
        savesKeys = listman.bubble_sort_dict(saves)
        nombres = []
        for key in savesKeys:
            nombres.append(characters[saves[key]["character"]]["name"])
        opc = menu.get_dyn_menu(menu_cargar_partida[0],savesKeys,menu_cargar_partida[2],20,[[20,nombres]])

        if opc == 0:
            estado = "principal"
    while estado == "nueva_partida":
        opc = menu.get_menu(menu_nueva_partida[0],menu_nueva_partida[1],menu_nueva_partida[2],25,[45,[1,nombre],[2,[str(10),"ATK: "],[str(10),"DEF: "],[str(10),"HP: "],[str(10),"SPD: "]],[3,energia]])
        if opc == 0: # Volver
            estado = "principal"
        elif opc == 1:
            nombre = char_manager.nuevo_nombre()
        elif opc == 3:
            energia = char_manager.tipo_energia()