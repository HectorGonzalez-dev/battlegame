
def bubble_sort(valores, orden="asc"):
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