# Non-OOP
# Bank Version 1
# Single account
nombre_cuenta = 'Joe' 
saldo_cuenta = 100 
contrasenia_cuenta = 'soup'
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
      contrasenia_usuario = input('Por favor introduce la contraseña: ')
      if contrasenia_usuario != contrasenia_cuenta:
        print('Contraseña incorrecta')
      else:
        print('Tu saldo es', saldo_cuenta)

  elif action == 'd':
      print('Deposito')
      cantidad_a_depositar = int(input('Por favor ingresa la cantidad a depositar: '))
      contrasenia_usuario = input('Por favor introduce la contraseña: ')
      if cantidad_a_depositar < 0:
        print('No puedes depositar una cantidad negativa!')
      elif contrasenia_usuario != contrasenia_cuenta:
        print('Contraseña incorrecta')
      else:  # OK
        saldo_cuenta = saldo_cuenta + cantidad_a_depositar
        print('Tu nuevo saldo es:', saldo_cuenta)

  elif action == 's':  # show
    print('Cuenta:')
    print('       Nombre', nombre_cuenta)
    print('       Saldo:', saldo_cuenta)
    print('       contraseña:', contrasenia_cuenta)
    print()

  elif action == 'w':
    print('Retiro:')
    cantidad_a_retirar = int(input('Por favor ingresa la cantidad a retirar: '))
    contrasenia_usuario = input('Por favor introduce la contraseña: ')
    if cantidad_a_retirar < 0:
        print('No puedes retirar una cantidad negativa')
    elif contrasenia_usuario != contrasenia_cuenta:
        print('Contraseña incorrecta')
    elif cantidad_a_retirar > saldo_cuenta:
        print('El saldo de tu cuenta no es suficiente')
    else:  #OK
        saldo_cuenta = saldo_cuenta - cantidad_a_retirar
        print('Tu nuevo saldo es:', saldo_cuenta)

  elif action == 'q':
    break

print('Bye')