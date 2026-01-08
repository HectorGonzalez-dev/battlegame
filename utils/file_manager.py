import json

# Función para obtener un json
def get_data(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_data(archivo, datos):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)