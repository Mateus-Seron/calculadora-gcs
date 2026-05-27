import unittest

<<<<<<< HEAD
from calc_potencia import potencia, raiz_quadrada, raiz_cubica

# Módulo B — Casos de testes para operações de potência

class TestesModuloCalcPotencia(unittest.TestCase):
    # Potencia
    def test_potencia_zero(self):
        self.assertEqual(potencia(2,0),1)

    def test_potencia_positivo(self):
        self.assertEqual(potencia(2,2),4)

    def test_potencia_negativa(self):
        self.assertEqual(potencia(2,-2),)
    
    # Raiz Quadrada
    def test_raiz_quadrada(self):
        self.assertEqual(raiz_quadrada(9),3)

    def test_raiz_negativo(self):
        with self.assertRaises(ValueError):
            raiz_quadrada(-9)

    # Raiz Cúbica
    def test_raiz_cubica_pos(self):
        self.assertEqual(raiz_cubica(8),2)

    def test_raiz_cubica_neg(self):
        self.assertEqual(raiz_cubica(-27),3)
=======
from calc_percentual import percentual, acrescimo, desconto
from calc_basico import somar, subtrair, multiplicar, dividir
from calc_estatistica import media, mediana, desvio_padrao
from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
from calc_potencia import potencia, raiz_quadrada, raiz_cubica

#Módulo A - Casos de Testes para opreações básicas
class TestesModuloCalcBasico(unittest.TestCase):
    # Soma: Caso de Sucesso
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)

    # Soma: Caso de Erro com string
    def test_somar_string(self):
        self.assertEqual(somar("a", 3), "Erro: os valores passados devem ser números.")
        self.assertEqual(somar(2, "b"), "Erro: os valores passados devem ser números.")
        self.assertEqual(somar("a", "b"), "Erro: os valores passados devem ser números.")

    # Subtração: Caso de Sucesso
    def test_subtrair(self):
        self.assertEqual(subtrair(5, 2), 3)

    # Subtração: Caso de Erro com string
    def test_subtrair_string(self):
        self.assertEqual(subtrair("a", 2), "Erro: os valores passados devem ser números.")
        self.assertEqual(subtrair(5, "b"), "Erro: os valores passados devem ser números.")
        self.assertEqual(subtrair("a", "b"), "Erro: os valores passados devem ser números.")

    # Multiplicação: Caso de Sucesso
    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)

    # Multiplicação: Caso de Erro com string
    def test_multiplicar_string(self):
        self.assertEqual(multiplicar("a", 3), "Erro: os valores passados devem ser números.")
        self.assertEqual(multiplicar(4, "b"), "Erro: os valores passados devem ser números.")
        self.assertEqual(multiplicar("a", "b"), "Erro: os valores passados devem ser números.")


    # Divisão: Caso de Sucesso
    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    # Divisão: Caso de Erro com string
    def test_dividir_string(self):
        self.assertEqual(dividir("a", 2), "Erro: os valores passados devem ser números.")
        self.assertEqual(dividir(10, "b"), "Erro: os valores passados devem ser números.")
        self.assertEqual(dividir("a", "b"), "Erro: os valores passados devem ser números.")

    # Divisão: Caso de Erro com divisão por zero
    def test_dividir_por_zero(self):
        self.assertEqual(dividir(10, 0), "Não é possível dividir por zero")

# Módulo B — Casos de testes para operações de potencia
class TestesModuloCalcPotencia(unittest.TestCase):

    # Potência: Caso de Sucesso
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    # Potência: Caso de Erro com base zero e expoente negativo
    def test_potencia_base_zero_expoente_negativo(self):
        self.assertEqual(potencia(0, -1), "Valores inválidos.")

    # Raiz Quadrada: Caso de Sucesso
    def test_raiz_quadrada(self):
        self.assertEqual(raiz_quadrada(16), 4)

    # Raiz Quadrada: Caso de Erro com valor negativo
    def test_raiz_quadrada_valor_negativo(self):
        self.assertEqual(raiz_quadrada(-1), "Valor negativo.")

    # Raiz Cúbica: Caso de Sucesso
    def test_raiz_cubica(self):
        self.assertEqual(raiz_cubica(27), 3)


# Módulo C — Casos de testes para operações percentuais
class TestesModuloCalcPercentual(unittest.TestCase):

    # Percentual: Caso de Sucesso
    def test_percentual(self):
        self.assertEqual(percentual(100, 10), 10)

    # Percentual: Caso de Erro com porcentagem negativa
    def test_percentual_porcentagem_negativa(self):
        with self.assertRaises(ValueError):
            percentual(100, -10)

    # Acréscimo: Caso de Sucesso
    def test_acrescimo(self):
        self.assertEqual(acrescimo(250, 25.50), 313.75)

    # Acréscimo: Caso de Erro com porcentagem negativa
    def test_acrescimo_porcentagem_negativa(self):
        with self.assertRaises(ValueError):
            acrescimo(250, -25.50)

    # Desconto: Caso de Sucesso
    def test_desconto(self):
        self.assertEqual(desconto(1, 10), 0.9)

    # Desconto: Caso de Erro com porcentagem negativa
    def test_desconto_porcentagem_negativa(self):
        with self.assertRaises(ValueError):
            desconto(1, -10)

# Módulo D — Casos de testes para operações de estatísticas
class TestesModuloCalcEstatistica(unittest.TestCase):

    # Media: Caso de Sucesso
    def test_media(self):
        self.assertEqual(media([5, 10, 15]), 10)

    # Media: Casos de Erro com lista vazia
    def test_media_lista_vazia(self):
        self.assertEqual(media([]), 0)

    # Media: Caso de Erro com lista contendo uma letra
    def test_media_lista_letra(self):
        self.assertEqual(media("a"), 0)

    # Mediana: Caso de Sucesso com número ímpar de elementos
    def test_mediana_impar(self):
        self.assertEqual(mediana([5, 10, 15]), 10)

    # Mediana: Caso de Sucesso com número par de elementos
    def test_mediana_par(self):
        self.assertEqual(mediana([5, 10, 15, 20]), 12.5)

    # Mediana: Caso de Erro com lista vazia
    def test_mediana_lista_vazia(self):
        self.assertEqual(mediana([]), 0)

    # Mediana: Caso de Erro com lista contendo uma letra
    def test_mediana_lista_letra(self):
        self.assertEqual(mediana("a"), 0)
    
    # Desvio Padrão: Caso de Sucesso
    def test_desvio_padrao(self):
        resultado = desvio_padrao([5, 10, 15, 20, 25])
        self.assertAlmostEqual(resultado, 7.0711, places=4)

    # Desvio Padrão: Caso de Erro com lista vazia
    def test_desvio_padrao_lista_vazia(self):
        self.assertEqual(desvio_padrao([]), 0)

    # Desvio Padrão: Caso de Erro com lista contendo uma letra
    def test_desvio_padrao_lista_letra(self):
        self.assertEqual(desvio_padrao("a"), 0)

# Módulo E — Casos de testes para operações de conversão
class TestesModuloCalcConversao(unittest.TestCase):

    # Celsius para Fahrenheit: Caso de Sucesso
    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(0), 32)

    # Celsius para Fahrenheit: Caso de Sucesso com valor negativo
    def test_celsius_para_fahrenheit(self):
        self.assertEqual(celsius_para_fahrenheit(-35.5), -31.9)

    # Km para Milhas: Caso de Sucesso
    def test_km_para_milhas(self):
        self.assertEqual(km_para_milhas(50), 31.05)

    # Kg para Libras: Caso de Erro com valor negativo
    def test_kg_para_libras_negativo(self):
        with self.assertRaises(ValueError):
            kg_para_libras(-50)

    # Kg para Libras: Caso de Sucesso
    def test_kg_para_libras(self):
        self.assertEqual(kg_para_libras(125.75), 277.153)

    # Kg para Libras: Caso de Erro com valor negativo
    def test_kg_para_libras_zero(self):
        with self.assertRaises(ValueError):
            kg_para_libras(-99.99)

if __name__ == "__main__":
    unittest.main()
>>>>>>> c5d89ba3f2730cd3abe4c34bd93d8be77f38e46a
