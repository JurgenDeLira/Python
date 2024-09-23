import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def resolver_inecuaciones(inecuacion1, inecuacion2):
    # Definir la variable
    x = sp.Symbol('x')

    # Resolver las inecuaciones
    solucion1 = sp.solve_univariate_inequality(inecuacion1, x, relational=False)
    solucion2 = sp.solve_univariate_inequality(inecuacion2, x, relational=False)

    # Intersección de las soluciones
    solucion_final = solucion1.intersect(solucion2)

    # Convertir la solución a intervalo y mostrar
    print(f"La solución de {inecuacion1} y {inecuacion2} es: {solucion_final}")

    # Crear un gráfico de la solución
    dibujar_solucion(solucion_final)

def dibujar_solucion(intervalo):
    # Extraer los límites del intervalo
    izq, der = intervalo.inf, intervalo.sup

    # Crear el dibujo con Matplotlib
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(izq - 1, der + 2, 1))
    ax.set_xlim(izq - 1, der + 1)
    ax.set_ylim(-1, 1)

    # Crear la línea numérica
    ax.axhline(0, color='black', linewidth=1)

    # Dibujar el intervalo como una línea con puntos abiertos o cerrados
    if intervalo.left_open:
        ax.plot(izq, 0, 'wo', markersize=10, markeredgecolor='black')  # Punto abierto
    else:
        ax.plot(izq, 0, 'bo', markersize=10)  # Punto cerrado

    if intervalo.right_open:
        ax.plot(der, 0, 'wo', markersize=10, markeredgecolor='black')  # Punto abierto
    else:
        ax.plot(der, 0, 'bo', markersize=10)  # Punto cerrado

    # Dibujar la línea que conecta los puntos
    ax.plot(np.linspace(izq, der, 100), np.zeros(100), 'b-', linewidth=2)

    # Etiquetar el gráfico
    plt.title(f"Solución: {intervalo}")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Definir las inecuaciones
    x = sp.Symbol('x')
    inecuacion1 = 3 + 2*x < 3*x
    inecuacion2 = 3*x <= 2*(2 + x)

    # Resolver y dibujar
    resolver_inecuaciones(inecuacion1, inecuacion2)