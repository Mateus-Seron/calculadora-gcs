# calc_percentual.py
# Módulo C — Operações Percentuais
# Autor: Lucas Gabriel de Almeida Souza
# Branch: feature/modulo-percentual

def percentual(valor, porcentagem):
    # Função que retorna o total correspondente à porcentagem de um valor.
    if porcentagem < 0:
        raise ValueError("Porcentagens negativas são inválidas.")
    return valor * porcentagem / 100

def acrescimo(valor, porcentagem):
    # Função que retorna o acréscimo de porcentagem aplicado em um valor.
    if porcentagem < 0:
        raise ValueError("Porcentagens negativas são inválidas.")
    return valor + percentual(valor, porcentagem)
    
def desconto(valor, porcentagem):
    # Função que retorna o desconto percentual aplicado em um valor.
    if porcentagem < 0:
        raise ValueError("Porcentagens negativas são inválidas.")
    return valor - percentual(valor, porcentagem)