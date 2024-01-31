nombre = input ("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))

if edad >= 18:
    print(f"{nombre}, sí puedes comprar cerveza.")
else:
    print(f"{nombre}, eres menor edad y no puedes comprar alcohol.")
    
    # True -> 1
    # False -> 0
    # and -> multiplicación
    # or -> suma
    
    # edad >= 18 and tiene_ine == True
    # 14 >= 18 and True == True
    # 0 and 1
    # 0 * 1 = 0
    # edad >= 18 and tiene_ine == True and nacionalidad == "mexicana" and nombre [0] == "g"
    