# Non-OOP Bank
# Version 4
# Any number of accounts - with lists
lista_nombres_cuentas = [] 
lista_saldos_cuentas = [] 
lista_contrasenias_cuentas = []
def nueva_cuenta(nombre, saldo, contrasenia):
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  lista_nombres_cuentas.append(nombre) 
  lista_saldos_cuentas.append(saldo) 
  lista_contrasenias_cuentas.append(contrasenia)

def show(numero_de_cuenta):
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  print('       Cuenta', numero_de_cuenta)
  print('       nombre', lista_nombres_cuentas[numero_de_cuenta])
  print('       saldo:', lista_saldos_cuentas[numero_de_cuenta])
  print('       contraseña:',lista_contrasenias_cuentas[numero_de_cuenta])
  print()

def obtener_saldo(numero_de_cuenta, contrasenia):
  global lista_nombres_cuentas, lista_saldos_cuentas, lista_contrasenias_cuentas
  if contrasenia != lista_contrasenias_cuentas[numero_de_cuenta]:
    print('Contraseña incorrecta')
    return None
  return lista_saldos_cuentas[numero_de_cuenta]

#  --- Nos saltamos las demás funciones ---
# Creamos dos cuentas de prueba
  
print("La cuenta de Joe es la cuenta numero:", len(lista_nombres_cuentas)) 
nueva_cuenta("Joe", 100, 'soup')
print("La cuenta de Mary es la cuenta numero :", len(lista_nombres_cuentas)) 
nueva_cuenta("Mary", 12345, 'nuts')

while True:
  print()
  print('Presiona b para obtener tu saldo') 
  print('Presiona d para hacer un deposito')
  print('Presiona w para hacer un retiro') 
  print('Presiona s para mostrar la cuenta') 
  print('Presiona q para salir')
  print()
  action = input('¿Qué te gustaría hacer? ')
  action = action.lower()  # forzamos las minúsculas
  print()
  if action == 'b':
    print('Obtener saldo:')
    user_numero_de_cuenta = input('Por favor ingresa tu número de cuenta')
    user_numero_de_cuenta = int(user_numero_de_cuenta)
    user_contrasenia = input('Por favor ingresa la contrasenia: ')
    saldo = obtener_saldo(user_numero_de_cuenta, user_contrasenia)
    if saldo is not None:
      print('Your saldo is:', saldo)
#   --- Nos saltamos parte del código principal ---
   
print('Bye')