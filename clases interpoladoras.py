import numpy as np

class PolinomioInterpolador:
    def __init__(self, puntos):
        """
        Inicializa el objeto PolinomioInterpolador.
        
        :param puntos: Lista de tuplas (x, y) que representan los puntos a interpolar.
        """
        self.puntos = puntos
        self.coeficientes = self.calcular_coeficientes()

    def calcular_coeficientes(self):
        """
        Calcula los coeficientes del polinomio de Lagrange.
        
        :return: Lista de coeficientes del polinomio.
        """
        n = len(self.puntos)
        coeficientes = np.zeros(n)

        # Calcular los coeficientes del polinomio de Lagrange
        for i in range(n):
            x_i, y_i = self.puntos[i]
            producto = 1.0
            for j in range(n):
                if i != j:
                    x_j, _ = self.puntos[j]
                    producto *= (x_i - x_j)

            coeficientes[i] = y_i / producto

        return coeficientes

    def evaluar(self, x):
        """
        Evalúa el polinomio interpolador en un punto x.
        
        :param x: Valor en el que se desea evaluar el polinomio.
        :return: Valor del polinomio en x.
        """
        n = len(self.puntos)
        resultado = 0.0

        # Calcular el valor del polinomio en x
        for i in range(n):
            x_i, _ = self.puntos[i]
            term = self.coeficientes[i]
            for j in range(n):
                if i != j:
                    x_j, _ = self.puntos[j]
                    term *= (x - x_j) / (x_i - x_j)
            resultado += term

        return resultado

# Ejemplo de uso:
if __name__ == "__main__":
    # Ingresar puntos para interpolar
    puntos_input = [(1, 2), (2, 3), (3, 5), (4, 4)]  # Ejemplo de puntos
    interpolador = PolinomioInterpolador(puntos_input)

    # Evaluar el polinomio en un punto
    valor_x = 2.5
    resultado = interpolador.evaluar(valor_x)
    print(f"El valor del polinomio interpolador en x = {valor_x} es: {resultado}")
