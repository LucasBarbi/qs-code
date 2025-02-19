import unittest
from empregado import Empregado

class testempregado(unittest.TestCase):

    def testValidarCargoPresidente(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="silva", cargo="presidente", salario=1)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )
    def testValidarCargoDiretor(self):
        empregado = Empregado(primeiro_nome="vinicius", sobrenome="da", cargo="diretor", salario=2)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )

    def testValidarCargoGerente(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="barbi", cargo="gerente", salario=3)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )
    def testValidarCargoPresidente(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="silva", cargo="presidente", salario=4)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )
    def testValidarCargoAnalista(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="silva", cargo="analista", salario=1000)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )
    def testValidarCargoAuxiliar(self):
        empregado = Empregado(primeiro_nome="bini", sobrenome="vin", cargo="auxiliar", salario=10)
        entrada = empregado.validar_cargo()
        esperado = True

        return self.assertEqual(
            entrada, 
            esperado
            )
    def testNomeCompleto(self):
        empregado = Empregado(primeiro_nome="lucas", sobrenome="silva", cargo="presidente", salario=1)
        entrada = empregado.gerar_nome_completo()
        esperado = "lucassilva"

        return self.assertEqual(
            entrada, 
            esperado
            )
    def testNomeCompleto(self):
        empregado = Empregado(primeiro_nome="bini", sobrenome="barbieri", cargo="presidente", salario=1)
        entrada = empregado.gerar_nome_completo()
        esperado = "lucassilva"

        return self.assertEqual(
            entrada, 
            esperado
            )