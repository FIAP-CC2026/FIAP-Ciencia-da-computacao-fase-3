import unittest

from colonia.previsao import ajustar_reta, prever, classificar_previsao
from colonia.regras import decidir


class TestPrevisao(unittest.TestCase):
    def test_exemplo_do_enunciado(self):
        a, b = ajustar_reta([8, 10, 12], [20, 25, 30])
        self.assertAlmostEqual(a, 2.5)
        self.assertAlmostEqual(b, 0)
        self.assertAlmostEqual(prever(a, b, 11), 27.5)

    def test_ajuste_com_dados_fora_de_uma_reta_perfeita(self):
        a, b = ajustar_reta([1, 2, 3], [2, 3, 5])
        self.assertAlmostEqual(a, 1.5)
        self.assertAlmostEqual(b, 1 / 3)
        self.assertAlmostEqual(prever(a, b, 4), 19 / 3)

    def test_historicos_invalidos(self):
        casos = [([], []), ([8], [20]), ([8, 10], [20]),
                 ([8, 8], [20, 25]), ([-8, 10], [20, 25]),
                 ([8, 10], [20, float('nan')]),
                 ([8, float('inf')], [20, 25]), ([8, '10'], [20, 25])]
        for vento, energia in casos:
            with self.subTest(vento=vento, energia=energia):
                with self.assertRaises(ValueError):
                    ajustar_reta(vento, energia)

    def test_vento_previsto_invalido(self):
        for vento in [-1, float('inf'), float('nan')]:
            with self.subTest(vento=vento):
                with self.assertRaises(ValueError):
                    prever(2.5, 0, vento)

    def test_previsao_integrada_a_decisao(self):
        a, b = ajustar_reta([8, 10, 12], [20, 25, 30])
        self.assertEqual(classificar_previsao(prever(a, b, 10)), 'favoravel')
        classificacao = classificar_previsao(prever(a, b, 8))
        self.assertEqual(classificacao, 'desfavoravel')
        self.assertEqual(decidir(40, 70, classificacao),
                         'MODO ECONOMIA: desligar sistemas não essenciais')


if __name__ == '__main__':
    unittest.main()
