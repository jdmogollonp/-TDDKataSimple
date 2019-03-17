from unittest import TestCase
import Estadistica

class EstaditicaTest(TestCase):
    def test_procesar_secuencia(self):
        self.assertEqual(Estadistica().procesar_secuencia(""),[0],"Cadena vacio")

    def test_procesar_secuencia_unacadena(self):
        self.assertEqual(Estadistica().procesar_secuencia("1"), [0], "Un numero")