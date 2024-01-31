def vender_cerveza(edad_cliente, cantidad_pagada):
    precio_cerveza = 25

    if edad_cliente < 18:
        print("Lo siento, no puedo vender cerveza a menores de 18 años.")
    else:
        cambio = cantidad_pagada - precio_cerveza

        if cambio == 0:
            print("Aquí está tu cerveza. Gracias, disfruta.")
        elif cambio > 0:
            print(f"Aquí está tu cerveza y tu cambio de {cambio} pesos. Gracias, disfruta.")
        else:
            print(f"Lo siento, no tienes suficiente dinero. Faltan {abs(cambio)} pesos.")

# Ejemplo de uso:
edad = int(input("¿Cuántos años tienes? "))
pago = float(input("¿Cuánto pagas por la cerveza? "))

vender_cerveza(edad, pago)