camino = input("¿Que camino quieres tomar?, el de la izquierda o el de la derecha? ").lower()

    

if camino == "izquierda" or camino == "izquierdo":
    lado = "Este camino te llevara a Acapulco"
elif camino == "derecha" or camino == "derecho":
    lado = "Este camino te llevara Mazatlán"
else:
    lado = "Lo siento, necesito que decidas entre cualquiera de las dos opciones"

    
print(f"{lado}")