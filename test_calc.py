import unittest

from calc_estatistica import media, mediana, desvio_padrao

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