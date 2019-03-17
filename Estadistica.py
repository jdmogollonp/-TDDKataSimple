__author__ = "assistant"

class Estadistica:
    def procesar_secuencia(self,cadena):
        if cadena == "":
            return [0, None, None]
        elif "," in cadena:
            numeros = cadena.split(",")
            return [len(numeros), int(min(numeros))]
        else:
            return [1, int(min(cadena)), int(max(cadena))]


