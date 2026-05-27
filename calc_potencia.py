# calc_potencia.py
# Módulo B — Operações de Potência
# Autor: Mariana Paulino da Silva
# Branch: feature/modulo-potencia

def potencia(base, expoente):
    if(not isinstance(base, (int, float)) or not isinstance(expoente, (int, float))):
        return "Erro: os valores passados devem ser números."
    if(base == 0 and expoente < 0):
        return "Valores inválidos."
    return base ** expoente

def raiz_quadrada(valor):
    if(not isinstance(valor, (int, float))):
        return "Erro: o valor passado deve ser um número."      
    if(valor < 0):
        return "Valor negativo."
    return valor ** (1/2)

def raiz_cubica(valor):
    if(not isinstance(valor, (int, float))):
        return "Erro: o valor passado deve ser um número."
    return valor ** (1/3)
