import unittest

from calc_estatistica import media, mediana, desvio_padrao

# Módulo D — Casos de testes para operações de estatísticas
class TestesModuloCalcEstatistica(unittest.TestCase):

    # Caso de Sucesso
    def test_media(self):
        self.assertEqual(media([5, 10, 15]), 10)

    # Casos de Erro com lista vazia
    def test_media_lista_vazia(self):
        self.assertEqual(media([]), 0)

    # Caso de Sucesso com número ímpar de elementos
    def test_mediana_impar(self):
        self.assertEqual(mediana([5, 10, 15]), 10)

    # Caso de Sucesso com número par de elementos
    def test_mediana_par(self):
        self.assertEqual(mediana([5, 10, 15, 20]), 12.5)

    # Caso de Erro com lista vazia
    def test_mediana_lista_vazia(self):
        self.assertEqual(mediana([]), 0)

    # Caso de Sucesso para desvio padrão
    def test_desvio_padrao(self):
        resultado = desvio_padrao([5, 10, 15, 20, 25])
        self.assertAlmostEqual(resultado, 7.0711, places=4)

    # Caso de Erro com lista vazia
    def test_desvio_padrao_lista_vazia(self):
        self.assertEqual(desvio_padrao([]), 0)

if __name__ == "__main__":
    unittest.main()