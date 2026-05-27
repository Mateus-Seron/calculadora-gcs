import unittest

from calc_percentual import percentual, acrescimo, desconto
from calc_estatistica import media, mediana, desvio_padrao

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

if __name__ == "__main__":
    unittest.main()