__author__ = "assistant"
from statistics import mean

class Estadistica:
    def procesar_secuencia(self,cadena):
        if cadena == "":
            return [0, None, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            suma = 0
            for num in numeros:
                suma = suma + int(num)
            promedio = suma/len(numeros)
            return [len(numeros), int(min(numeros)), int(max(numeros)), promedio]
        else:
            return [1, int(cadena), int(cadena), int(cadena)]


