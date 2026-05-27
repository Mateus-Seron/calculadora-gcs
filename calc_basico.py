# Módulo A - Cálculos Básicos
# Autor: João Vitor Costa Braga
# Branch: feature/modulo-basico

def somar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Erro: os valores passados devem ser números."

    return a + b


def subtrair(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Erro: os valores passados devem ser números."

    return a - b


def multiplicar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Erro: os valores passados devem ser números."

    return a * b


def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Erro: os valores passados devem ser números."

    if b == 0:
        return "Erro: não é possível dividir por zero."

    return a / b