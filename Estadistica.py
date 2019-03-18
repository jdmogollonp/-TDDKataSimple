__author__ = "assistant"
from statistics import mean

class Estadistica:
    def procesar_secuencia(self,cadena):
        if cadena == "":
            return [0, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros), int(min(numeros)), int(max(numeros))]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]


