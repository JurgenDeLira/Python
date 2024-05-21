# Mayor o Menor
# Importamos la libreria random, la cual nos ayudará a obtener valores al azar.
import random

#Constantes de las cartas
TUPLA_PALO = ('Espadas', 'Corazones', 'Picas', 'Diamantes')
TUPLA_RANGO = ('As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Reina', 'Rey')

NCARTAS = 8

#Función que regresa una carta aleatoria del mazo
def obtener_carta(lista_de_cartas):
    carta = lista_de_cartas.pop() # Saca una carta de la parte superior del mazo y la devuelve
    return carta

#Función que devuelve una copia barajada del mazo
def mazo_barajeado(lista_de_cartas):
    mazo_de_salida = lista_de_cartas.copy() # Crea una copia del mazo inicial
    random.shuffle(mazo_de_salida)
    return mazo_de_salida

# Main Code
print('Bienvenido al juego Mayor o Menor.')
print('En este juego tendrás que elegir si la próxima carta mostrada será mayor o menro a la carta actual.')
print('Acertar la predicción te añade 20 puntos; fallar la predicción te hará perder 15 puntos.')
print('Tienes 50 puntos al iniciar')
print()

lista_mazo_inicial = []

for palo in TUPLA_PALO:
    for valor, rango in enumerate(TUPLA_RANGO):
        carta_dicc = {'rango': rango, 'palo': palo, 'valor': valor + 1}
        lista_mazo_inicial.append(carta_dicc)

puntuacion = 50

while True: #Se ejecuta multiples veces
    print()
    mazo_de_juego = mazo_barajeado(lista_mazo_inicial)
    carta_actual = obtener_carta(mazo_de_juego)
    rango_carta_actual = carta_actual['rango']
    valor_carta_actual = carta_actual['valor']
    palo_carta_actual = carta_actual['palo']
    print(f'La carta inicial es: {rango_carta_actual} de {palo_carta_actual}')

    for numero_de_cartas in range(0, NCARTAS): #Jugar una partida con esta cantidad de cartas
        respuesta = input(f'¿La próxima carta será mayor o menor que {rango_carta_actual} de {palo_carta_actual}? (ingresa ma o me):')
        respuesta = respuesta.casefold() #Forza a estar en minúsculas
        proxima_carta = obtener_carta(mazo_de_juego)
        rango_proxima_carta = proxima_carta['rango']
        palo_proxima_carta = proxima_carta['palo']
        valor_proxima_carta = proxima_carta['valor']
        print(f'La próxima carta es: {rango_proxima_carta} de {palo_proxima_carta}')

        if respuesta == 'ma':
            if valor_proxima_carta > valor_carta_actual:
                print('¡Felicidades! acertaste')
                puntuacion = puntuacion + 20
            else:
                print('lo siento, te equivocaste')
                puntuacion = puntuacion - 15
            
        elif respuesta == 'me':
            if valor_proxima_carta < valor_carta_actual:
                print('¡Felicidades! acertaste')
                puntuacion = puntuacion + 20
            else:
                print('Lo siento, te equivocaste')
                puntuacion = puntuacion - 15

        print(f'Tu puntuación es: {puntuacion}\n')
        rango_carta_actual = rango_proxima_carta
        valor_carta_actual = valor_proxima_carta
        palo_carta_actual = palo_proxima_carta
    
    jugar_de_nuevo = input('Para volver a jugar, presiona ENTER, o presiona "q" para salir: ')
    if jugar_de_nuevo == 'q':
        break

print('Bye!')