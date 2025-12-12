import json

# Función para obtener los personajes
def get_characters():
    with open("data/characters.json", "r", encoding="utf-8") as f:
        return json.load(f)