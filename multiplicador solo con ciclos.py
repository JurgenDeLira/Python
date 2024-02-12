"""Cree un programa que pida al usuario dos números enteros e imprima el resultado de su
multiplicación sin utilizar el operador de multiplicación (*). Puede utilizar ciclos y operaciones de suma.""" 

def multiplicacion_op(num1, num2):
    resultado = 0
    
    for i in range(num2):
        resultado = resultado + num1
        
    return resultado

num1 = int(input("Dame un número entero: "))
num2 = int(input("Dame otro número entero: "))
multiplicacion = multiplicacion_op(num1,num2)
print(f"la multiplicación de {num1} x {num2} da como resultado: {multiplicacion}")
