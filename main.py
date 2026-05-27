# main.py — importa módulos conforme são mergeados na main
from calc_basico import somar, subtrair, multiplicar, dividir
from calc_potencia import potencia, raiz_quadrada, raiz_cubica
from calc_percentual import percentual, acrescimo, desconto
from calc_estatistica import media, mediana, desvio_padrao
from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras


def menu():
    print("=== Calculadora GCS ===\n")

    try:
        print("Módulo Básico.")
        print("  2 + 3 =", somar(2, 3))
        print("  5 - 2 =", subtrair(5, 2))
        print("  4 * 3 =", multiplicar(4, 3))
        print("  10 / 2 =", dividir(10, 2))
    except ImportError:
        print("Módulo Básico ainda não disponível.")

    try:
        print("Módulo Potência.")
        print("  2^10 =", potencia(2, 10))
        print("  raiz(16) =", raiz_quadrada(16))
        print("  raiz cubica(27) =", raiz_cubica(27))
    except ImportError:
        print("Módulo Potência ainda não disponível.")

    try:
        print("Módulo Percentual.")
        print("  10% de 200 =", percentual(200, 10))
        print("  200 + 10% =", acrescimo(200, 10))
        print("  200 - 10% =", desconto(200, 10))
    except ImportError:
        print("Módulo Percentual ainda não disponível.")

    try:
        dados = [5, 10, 15, 20, 25]
        print("Módulo Estatística.")
        print("  média", dados, "=", media(dados))
        print("  mediana", dados, "=", mediana(dados))
        print("  desvio padrão", dados, "=", round(desvio_padrao(dados), 4))
    except ImportError:
        print("Módulo Estatística ainda não disponível.")

    try:
        print("Módulo Conversão.")
        print("  0°C =", celsius_para_fahrenheit(0), "°F")
        print("  1 km =", km_para_milhas(1), "milhas")
        print("  1 kg =", kg_para_libras(1), "libras")
    except ImportError:
        print("Módulo Conversão ainda não disponível.")


if __name__ == "__main__":
    menu()
