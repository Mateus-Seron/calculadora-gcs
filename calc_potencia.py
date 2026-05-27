# calc_potencia.py
# Módulo B — Operações de Potência
# Autor: Mariana Paulino da Silva
# Branch: feature/modulo-potencia

def potencia(base, expoente):
    if(base == 0 and expoente < 0):
        return "Valores inválidos."
    return base ** expoente

def raiz_quadrada(valor):
    if(valor < 0):
        return "Valor negativo."
    return valor ** (1/2)

def raiz_cubica(valor):
    return valor ** (1/3)
