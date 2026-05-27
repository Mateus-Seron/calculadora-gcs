#Módulo A - Cálculos Básicos
#Autor: João Vitor Costa Braga
# Branch: feature/modulo-basico


def soma(a, b):
    try:
        return a + b
    except TypeError:
        return "Erro: os valores passados devem ser números."


def subtracao(a, b):
    try:
        return a - b
    except TypeError:
        return "Erro: os valores passados devem ser números."


def multiplicacao(a, b):
    try:
        return a * b
    except TypeError:
        return "Erro: os valores passados devem ser números."


def divisao(a, b):
    try:
        if b == 0:
            raise ValueError("Não é possível dividir por zero")

        return a / b
    except TypeError:
        return "Erro: os valores passados devem ser números."