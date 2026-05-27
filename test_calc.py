import unittest

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