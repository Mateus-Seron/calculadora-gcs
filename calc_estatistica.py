# calc_estatistica.py
# Módulo D — Operações de estatísticas
# Autor: Enzo Euvine Cunha Neves
# Branch: feature/modulo-estatistica

def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista) 

def mediana(lista):
    if not lista:
        return 0
    sorted_lista = sorted(lista)
    n = len(sorted_lista)
    if n % 2 == 0:
        return (sorted_lista[n//2 - 1] + sorted_lista[n//2]) / 2
    else:
        return sorted_lista[n//2]

def desvio_padrao(lista):
    if not lista:
        return 0
    m = media(lista)
    squared_diffs = [(x - m) ** 2 for x in lista]
    return (sum(squared_diffs) / len(lista)) ** 0.5


