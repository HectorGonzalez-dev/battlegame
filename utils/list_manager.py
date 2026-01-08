
def bubble_sort_list(valores, orden="asc"):
    lista = valores.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if orden == "asc":
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:  # desc
                if lista[j] < lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def bubble_sort_dict(dicc, orden="asc", key=""):
    keys = list(dicc.keys())
    n = len(keys)

    for i in range(n):
        for j in range(0, n - i - 1):
            if key == "":
                val1 = keys[j]
                val2 = keys[j + 1]
            else:
                val1 = dicc[keys[j]][key]
                val2 = dicc[keys[j + 1]][key]

            if orden == "asc":
                if val1 > val2:
                    keys[j], keys[j + 1] = keys[j + 1], keys[j]
            else:  # desc
                if val1 < val2:
                    keys[j], keys[j + 1] = keys[j + 1], keys[j]
    return keys