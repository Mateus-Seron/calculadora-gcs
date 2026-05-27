# calc_conversao.py
# Módulo E — Operações de Conversão
# Autor: Lucas Gabriel de Almeida Souza
# Branch: feature/modulo-conversao

def celsius_para_fahrenheit(celsius):
    # Função que retorna a conversão de Celsius para Fahrenheit.
    return (celsius * 9/5) + 32

def km_para_milhas(km):
    # Função que retorna a conversão de quilômetros para milhas.
    if km < 0:
        raise ValueError("Valores negativos são inválidos.")
    return km * 0.621

def kg_para_libras(kg):
    # Função que retorna a conversão de quilogramas para libras.
    if kg < 0:
        raise ValueError("Valores negativos são inválidos.")
    return kg * 2.204