import pygame #Librería principal
import sys # Manipular cosas bpasicas del OS
import random # Generar valores aleatorios

#Inicializar la librería pygame
pygame.init()

# Si el nombre de la variable
#Define el alto de la pantalla
PANTALLA_ALTO : int = 600 # En python puedes tipar, pero no es necesario
#Define largo pantalla
PANTALLA_LARGO : int = 800

#Define el color de fondo
BACKGROUND_COLOR = (43, 43, 43) #Esto es una tupla
#las tuplas no cambian, las listas si

#Define color de pelota
BALL_COLOR = (255, 255, 255)



#Rapidez de la pelota
BALL_SPEED = [5,5]

#Se guarda la pantalla
screen = pygame.display.set_mode((PANTALLA_LARGO, PANTALLA_ALTO))

#Se guarda la pelota
ball = pygame.Rect(PANTALLA_LARGO // 2, PANTALLA_ALTO // 2, 20, 20)

# Variable que contendrá el reloj interno del juego
clock = pygame.time.Clock()

# Función para que la pelota se mueva
def ball_move():
    ball.x += BALL_SPEED[0]
    ball.y += BALL_SPEED[1]

clock = pygame.time.Clock()

# Variable que definirá el estado de mi juego
running = True

# Bucle principal del juego
while running:
   
   #Detectar las teclas que el usuario presionó
    for event in pygame.event.get():
        
        #Si se presiona el botón de "exit" se sale del juego y cierra la ventan
        if event.type == pygame.QUIT:
            running = False
    
    #Llamar la clase ball_move()
    ball_move()
    
    # Rellenamos nuestra pantalla de algún color
    screen.fill(BACKGROUND_COLOR)
    
    #Dibujar la pelota
    pygame.draw.ellipse(screen,BALL_COLOR, ball)
    
    #Actualizabamos la pantalla
    pygame.display.flip()
    clock.tick(60)
    
#Cerramos el juego    
pygame.quit()
sys.exit()

