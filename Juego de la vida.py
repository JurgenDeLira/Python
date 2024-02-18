# Importamos las librerías necesarias para nuestro código
import pygame, sys #Este paquete nos ayudará a crear una interfaz gráfica, SE DEBE DE DESCARGAR
import numpy # Nos ayudará a hacer cálculos matemáticos. SE DEBE DE DESCARGAR
import time # Medirá el tiempo de las células
import random

# Inicializamos pygame
pygame.init()

# Estas variables deinirán el tamaño de la plantalla
alto_pantalla = 700
largo_pantalla = 700

# Creamos una variable que controla la pantalla
screen = pygame.display.set_mode((alto_pantalla, largo_pantalla))

bgColor = 61,61,100

screen.fill(bgColor)

# Definimos el número de celdas disponibles en el tablero
numero_celdas_y = 25
numero_celdas_x = 25

celda_altura = alto_pantalla / numero_celdas_y
celda_anchura = largo_pantalla / numero_celdas_x

gameState = numpy.zeros((numero_celdas_x, numero_celdas_y))

running = True
"""for i in range(0,100):
    pos_x = random.randint(0, 24)
    pos_y = random.randint(0, 24)
    
    gameState[pos_x, pos_y] = 1
    

gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1

gameState[21,21] = 1

gameState[22,22] = 1

gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1
"""

pausa = False


#Bucle principal de nuestro juego será infinito ya que es True, esto siempre hará que sea infinito
while running:
        #Realizamos una copia de la matíz anterior para realizar los cálculos
    newGameState = numpy.copy(gameState)
    
    #Este ciclo será el que termine la ejecución de mi juego cuando se presiona la X en la ventana
    #El pygame.quit: esta dictando que running seaS False y asi cuando presionas la tacha ya se quita
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:#Detecta backspace
            pausa = not pausa
            
        mouse_click = pygame.mouse.get_pressed()
        
        if sum(mouse_click) > 0:
            posicion_x, posicion_y = pygame.mouse.get_pos() #Me dara la posición relativa de mi mouse
            
            posicion_celda_x = int(numpy.floor(posicion_x / celda_anchura))
            posicion_celda_y = int(numpy.floor(posicion_y / celda_altura))
            print(posicion_celda_x, posicion_celda_y)
            
            if posicion_celda_x > (numero_celdas_x - 1):
                posicion_celda_x = (numero_celdas_x -1)
                
            elif posicion_celda_y > (numero_celdas_y - 1):
                posicion_celda_y = (numero_celdas_y - 1)
                
            if gameState[posicion_celda_x, posicion_celda_y] == 0:
                newGameState[posicion_celda_x, posicion_celda_y] = 1
                
            elif gameState[posicion_celda_x, posicion_celda_y] == 1:
                newGameState[posicion_celda_x, posicion_celda_y] = 0
                
            

    
            #Se va a encargar de recorrer nuestra cuadricula para saber si una esta muerta o viva
            #O sea hacemos dos ciclos for (aninados) para recorrer el "tablero" del juego
    for y in range(0, numero_celdas_y):
        for x in range(0, numero_celdas_x):
            
            if not pausa:
                # Hacemos elcálculo del número de vecinos que tenemos en cada una de nuestras celdas
                numero_vecinos = 	gameState[((x-1)	% numero_celdas_x ,  (y-1)		% numero_celdas_y)] + \
                                    gameState[(x 		% numero_celdas_x ,  (y-1)		% numero_celdas_y)] + \
                                    gameState[((x + 1)	% numero_celdas_x ,  (y-1)		% numero_celdas_y)] + \
                                    gameState[((x + 1)	% numero_celdas_x ,   y			% numero_celdas_y)] + \
                                    gameState[(x		% numero_celdas_x ,  (y+1)		% numero_celdas_y)]	+ \
                                    gameState[((x-1)	% numero_celdas_x ,  (y+1)		% numero_celdas_y)] + \
                                    gameState[((x - 1)	% numero_celdas_x ,  (y)		% numero_celdas_y)] + \
                                    gameState[((x + 1)	% numero_celdas_x ,  (y + 1)	% numero_celdas_y)]
                
                #Establecemos las reglas del juego
                #Evalua si mi célula está muerta y puede revivir
                if gameState[x, y] == 0 and numero_vecinos == 3:
                    newGameState[x ,y] = 1 #Celula revive
                    
                    #Evalua si la célula está viva y tiene menos de 2 o más de 3 vecinos
                elif gameState[x, y] == 1 and (numero_vecinos < 2 or numero_vecinos > 3):
                    newGameState[x,y] = 0 #Célula muere
        
    #Axtualizamos el juego
    gameState = numpy.copy(newGameState)
    
    screen.fill(bgColor)
            
    #Hacemos dos cicloss for (anidados) para dibujar el "tablero" del juego
    for y in range(0, numero_celdas_y):
        for x in range(0, numero_celdas_x):
            poly = [
                (x * celda_anchura,			 	y * celda_altura),
                ((x+1) * celda_anchura,		 	y * celda_altura),
                ((x+1) * celda_anchura, 	(y+1) * celda_altura),
                (x * celda_anchura, 		(y+1) * celda_altura)
                    ]
            
            if gameState[x,y] == 0:
                pygame.draw.polygon(screen, (255, 255 ,255), poly, 1) # el 1 es un pixel de anchura
            elif gameState[x,y] == 1:
                pygame.draw.polygon(screen, (255, 255 ,255), poly, 0)
            
            
    
    # Actualizamos la pantalla
    
    pygame.display.flip()
    time.sleep(0.1)

pygame.quit()