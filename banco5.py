lista_cuentas = [] 

def nueva_cuenta(a_name, a_saldo, a_contrasenia):
  global lista_cuentas
  nueva_cuenta_dic = {'name': a_name, 'balance': a_saldo, 'password': a_contrasenia}
  lista_cuentas.append(nueva_cuenta_dic)  # 2

def show(numero_de_cuenta):
  global lista_cuentas
  print('Account', numero_de_cuenta)
  this_cuenta_dic = lista_cuentas[numero_de_cuenta]
  print('       Nombre:', this_cuenta_dic['name'])
  print('       Saldo:', this_cuenta_dic['balance'])
  print('       Contraseña:', this_cuenta_dic['password'])
  print()

def obtener_saldo(numero_de_cuenta, contrasenia):
  global lista_cuentas
  this_cuenta_dic = lista_cuentas[numero_de_cuenta]  # 3
  if contrasenia != this_cuenta_dic['password']:
    print('Contraseña incorrecta')
    return None
  return this_cuenta_dic['balance']

# Otras funciones como deposito() y retiro() no se mostraron para ser mas breves

# Creamos dos cuentas de prueba
print("Numero de cuenta de Joe:", len(lista_cuentas))
nueva_cuenta("Joe", 100, 'soup')
print("Numero de cuenta de Mary:", len(lista_cuentas))
nueva_cuenta("Mary", 12345, 'nuts')

while True:
  print()
  print('Presiona b para obtener tu saldo') 
  print('Presiona d para hacer un deposito')
  print('Presiona w para hacer un retiro') 
  print('Presiona s para mostrar la cuenta') 
  print('Presiona n para crear una nueva cuenta')
  print('Presiona q para salir')
  print()
  action = input('¿Qué te gustaría hacer? ')
  action = action.lower()

  if action == 'b':
    print('Obtener saldo:')
    user_numero_de_cuenta = int(input('Por favor ingresa el número de cuenta: '))
    user_contrasenia = input('Por favor ingresa la contraseña: ')
    saldo = obtener_saldo(user_numero_de_cuenta, user_contrasenia)
    if saldo is not None:
        print('Tu saldo es:', saldo)
  elif action == 'd':
    print('Deposito:')
    user_numero_de_cuenta = int(input('Por favor ingresa el número de cuenta: '))
    user_cantidad_depositar = int(input('Por favor ingresa la cantidad a depositar: '))
    user_contrasenia = input('Por favor ingresa la contraseña: ')
    # Llama la función deposito() aquí
    # nuevo_saldo = deposit(user_numero_de_cuenta, user_cantidad_depositar, user_contrasenia)
    # if nuevo_saldo is not None:
    #     print('Tu nuevo saldo es:', nuevo_saldo)
    print("Esta función aun no se ha implementado")
  elif action == 'n':
    print('Nueva cuenta:')
    nombre_usuario = input('Ingres tu nombre: ')
    user_cantidad_inicial = int(input('Ingresa la cantidad a depositar para abrir tu cuenta: '))
    user_contrasenia = input('Ingres tu contraseña: ')
    user_numero_de_cuenta = len(lista_cuentas)
    nueva_cuenta(nombre_usuario, user_cantidad_inicial, user_contrasenia)
    print('Tu número de cuenta es:', user_numero_de_cuenta)
  elif action == 'q':
    break
  else:
    print('Acción invalida.')

#   --- Nos saltamos funciones principales ---

print('Bye')