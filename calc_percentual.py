# calc_percentual.py
# Módulo C — Operações Percentuais
# Autor: Lucas Gabriel de Almeida Souza
# Branch: feature/modulo-c

def percentual(valor, porcentagem):
    # Função que retorna o total correspondente à porcentagem de um valor.
    return valor * porcentagem / 100

def acrescimo(valor, porcentagem):
    # Função que retorna o acréscimo de porcentagem aplicado em um valor.
    return valor + percentual(valor, porcentagem)
    
def desconto(valor, porcentagem):
    # Função que retorna o desconto percentual aplicado em um valor.
    return valor - percentual(valor, porcentagem)