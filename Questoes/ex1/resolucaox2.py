
import unittest
from solution import retorna_tempo_arena_em_milisegundos
class Test(unittest.TestCase):
  def test_retorna_tempo_arena_em_milisegundos_deve_calcular_com_distancia_de_quatrocentos_e_cinquenta_metros(self):
    self.assertEqual(retorna_tempo_arena_em_milisegundos("0.45",340), 1324)