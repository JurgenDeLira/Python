color = input("Dame el color de la pelota: ").lower()

if color == "roja" or color == "amarilla":
    print("Puse la pelota en el montón rojo/amarillo")
elif color == "azul" or color =="morada":
    print("Puse la pelota en el montón azul/morado")

else:
    print("Puse la pelota en el montón multicolor")