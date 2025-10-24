"""
Testes unitários para o script de pipeline
"""

import unittest
from pipe import somar, multiplicar, processar_dados


class TestOperacoesBasicas(unittest.TestCase):
    """Testes para operações matemáticas básicas"""
    
    def test_somar_positivos(self):
        """Testa soma de números positivos"""
        self.assertEqual(somar(10, 5), 15)
        self.assertEqual(somar(3, 7), 10)
    
    def test_somar_negativos(self):
        """Testa soma com números negativos"""
        self.assertEqual(somar(-5, -3), -8)
        self.assertEqual(somar(-10, 5), -5)
    
    def test_somar_zero(self):
        """Testa soma com zero"""
        self.assertEqual(somar(0, 0), 0)
        self.assertEqual(somar(5, 0), 5)
    
    def test_multiplicar_positivos(self):
        """Testa multiplicação de números positivos"""
        self.assertEqual(multiplicar(10, 5), 50)
        self.assertEqual(multiplicar(3, 7), 21)
    
    def test_multiplicar_por_zero(self):
        """Testa multiplicação por zero"""
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(0, 10), 0)
    
    def test_multiplicar_negativos(self):
        """Testa multiplicação com números negativos"""
        self.assertEqual(multiplicar(-5, 3), -15)
        self.assertEqual(multiplicar(-4, -2), 8)


class TestProcessamentoDados(unittest.TestCase):
    """Testes para processamento de dados"""
    
    def test_processar_lista_simples(self):
        """Testa processamento de lista simples"""
        numeros = [1, 2, 3, 4, 5]
        resultado = processar_dados(numeros)
        
        self.assertEqual(resultado['soma'], 15)
        self.assertEqual(resultado['quantidade'], 5)
        self.assertEqual(resultado['media'], 3.0)
    
    def test_processar_lista_unico_elemento(self):
        """Testa processamento com um único elemento"""
        numeros = [10]
        resultado = processar_dados(numeros)
        
        self.assertEqual(resultado['soma'], 10)
        self.assertEqual(resultado['quantidade'], 1)
        self.assertEqual(resultado['media'], 10.0)
    
    def test_processar_lista_vazia(self):
        """Testa processamento de lista vazia"""
        numeros = []
        resultado = processar_dados(numeros)
        
        self.assertEqual(resultado['soma'], 0)
        self.assertEqual(resultado['quantidade'], 0)
        self.assertEqual(resultado['media'], 0)
    
    def test_processar_numeros_negativos(self):
        """Testa processamento com números negativos"""
        numeros = [-5, -10, -15]
        resultado = processar_dados(numeros)
        
        self.assertEqual(resultado['soma'], -30)
        self.assertEqual(resultado['quantidade'], 3)
        self.assertEqual(resultado['media'], -10.0)
    
    def test_processar_numeros_decimais(self):
        """Testa processamento com números decimais"""
        numeros = [1.5, 2.5, 3.0]
        resultado = processar_dados(numeros)
        
        self.assertEqual(resultado['soma'], 7.0)
        self.assertEqual(resultado['quantidade'], 3)
        self.assertAlmostEqual(resultado['media'], 2.333, places=2)


if __name__ == '__main__':

    unittest.main(verbosity=2)