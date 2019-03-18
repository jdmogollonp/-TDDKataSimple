__author__ = "assistant"
from statistics import mean

class Estadistica:
    def procesar_secuencia(self,cadena):
        if cadena == "":
            return [0, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            suma = int(numeros[0]) + int(numeros[1])
            promedio = suma/len(numeros)
            return [len(numeros), int(min(numeros)), int(max(numeros)), promedio]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]


