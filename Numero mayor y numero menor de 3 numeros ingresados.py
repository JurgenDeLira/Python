"""Cree un programa que pida al usuario tres números enteros distintos y luego determine
e imprima el número mayor y el número menor entre ellos. Ejemplo: 'El número mayor es 7.
El número menor es 3'. No importa el orden en que el usuario ingrese los números."""

def mayor(num1, num2, num3):
    if num1 > num2 or num1 > num3:
     mayor = num1
    elif num2 > num1 or num2 > num3:
      mayor = num2
    elif num3 > num1 or num3 > num2:
      mayor = num3
    return mayor

def menor(num1, num2, num3):
    if num1 < num2 or num1 < num3:
     menor = num1
    elif num2 < num1 or num2 < num3:
     menor = num2
    elif num3 < num1 or num3 < num2:
     menor = num3
    return menor


num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa un segundo número entero: "))
num3 = int(input("Ingresa un tercer número entero: "))

NumeroMayor = mayor(num1, num2, num3)
NumeroMenor = menor(num1, num2, num3)

print(f"El número mayor es {NumeroMayor}. El número menor es {NumeroMenor}.")