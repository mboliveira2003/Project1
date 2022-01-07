#! /usr/bin/env python3
import unittest
from esparsa import *
class TestPosicao(unittest.TestCase):
	def test_1(self):
		self.assertRaises(ValueError, cria_posicao, -1, -1)
	def test_2(self):
		self.assertIsNotNone(cria_posicao(1,2))
	def test_3(self):
		self.assertTrue(eh_posicao(cria_posicao(1, 2)))
	def test_4(self):
		self.assertFalse(eh_posicao(1.2))
	def test_5(self):
		self.assertEqual(1, posicao_linha(cria_posicao(1, 2)))
	def test_6(self):
		self.assertEqual(2, posicao_coluna(cria_posicao(1, 2)))
	def test_7(self):
		self.assertTrue(posicao_igual(cria_posicao(1, 2), cria_posicao(1, 2)))
	def test_8(self):
		self.assertFalse(posicao_igual(cria_posicao(1, 2), cria_posicao(2, 1)))
	def test_9(self):
		self.assertEqual('(1, 2)', posicao_str(cria_posicao(1, 2)))
	def test_10(self):
		self.assertRaises(ValueError, cria_posicao, 1, -12)
	def test_11(self):
		self.assertRaises(ValueError, cria_posicao, (), ())
	def test_12(self):
		self.assertIsNotNone(cria_posicao(1000,0))

class TestMatriz(unittest.TestCase):
	def test_1(self):
		self.assertIsNotNone(cria_matriz())
	def test_2(self):
		self.assertIsNotNone(cria_matriz(1.0))
	def test_3(self):
		self.assertTrue(eh_matriz(cria_matriz()))
	def test_4(self):
		self.assertFalse(eh_matriz(1.0))
	def test_5(self):
		self.assertAlmostEqual(0.0, matriz_zero(cria_matriz()))
	def test_6(self):
		self.assertAlmostEqual(1.5,matriz_zero(cria_matriz(1.5)))
	def test_7(self):
		self.assertAlmostEqual(2.0, matriz_zero(matriz_copia(cria_matriz(2))))
	def test_8(self):
		self.assertTrue(eh_matriz(matriz_copia(cria_matriz())))
	def test_9(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 12.5))
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(2,1), 5))
	def test_10(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 5))
		self.assertAlmostEqual(5.0, matriz_valor(mat, cria_posicao(1,2)))
	def test_11(self):
		self.assertEqual((), matriz_dimensao(cria_matriz()))
	def test_12(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 5))
		dim = matriz_dimensao(mat)
		self.assertEqual('(1, 2)', posicao_str(dim[0]))
		self.assertEqual('(1, 2)', posicao_str(dim[1]))
	def test_13(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 12.5))
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(2,1), 5))
		self.assertAlmostEqual(0.5, matriz_densidade(mat))
	def test_14(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 12.5))
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(2,1), 5))
		matriz_nulo(mat, 12.5)
		self.assertAlmostEqual(1.0, matriz_densidade(mat))
	def test_15(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 12.5))
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(2,1), 5))
		self.assertEqual("0.0 12.5\n5.0 0.0", matriz_str(mat, "%.1f"))
	def test_16(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 12.5))
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(2,1), 5))
		self.assertEqual((0.0, 12.5), matriz_linha(mat, 1))
	def test_17(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 12.5))
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(2,1), 5))
		self.assertEqual((12.5, 0.0), matriz_coluna(mat, 2))
	def test_18(self):
		mat = cria_matriz()
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(1,2), 12.5))
		self.assertAlmostEqual(0.0, matriz_posicao(mat, cria_posicao(2,1), 5))
		self.assertEqual((0.0, 0.0), matriz_diagonal(mat))

if __name__ == '__main__':
	from os import getenv
	if getenv('TAD'):
		exec(f"from {getenv('TAD')} import *")
	unittest.main()
