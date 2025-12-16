import json

# Función para obtener los personajes
def get_data(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)