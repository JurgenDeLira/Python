import numpy as np

# Función para sumar dos polinomios manualmente
def suma_polinomios_manual(p1, p2):
    # Asegurar que ambos polinomios tengan el mismo grado (rellenamos con ceros si es necesario)
    if len(p1) < len(p2):
        p1 = [0] * (len(p2) - len(p1)) + p1
    elif len(p2) < len(p1):
        p2 = [0] * (len(p1) - len(p2)) + p2

    # Sumar los coeficientes de ambos polinomios
    suma = [coef1 + coef2 for coef1, coef2 in zip(p1, p2)]
    return suma

# Función para sumar dos polinomios usando numpy
def suma_polinomios_numpy(p1, p2):
    return np.polyadd(p1, p2)

# Función principal para recibir dos polinomios y sumarlos de ambas maneras
def main():
    # Ejemplo de polinomios
    p1 = [3, 4, 2]  # Representa 3x^2 + 4x + 2
    p2 = [5, -3, 1, 7]  # Representa 5x^3 - 3x^2 + x + 7

    print(f"Polinomio 1: {p1}")
    print(f"Polinomio 2: {p2}")

    # Suma manual
    suma_manual = suma_polinomios_manual(p1, p2)
    print(f"Suma manual: {suma_manual}")

    # Suma usando numpy
    suma_numpy = suma_polinomios_numpy(p1, p2)
    print(f"Suma usando numpy: {suma_numpy}")

if __name__ == "__main__":
    main()