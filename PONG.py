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

# Función para que la pelota se mueva
def ball_move():
    ball.x += BALL_SPEED[0]
    ball.y += BALL_SPEED[1]

clock = pygame.time.Clock()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    ball_move()
    
    screen.fill(BACKGROUND_COLOR)
    
    pygame.draw.ellipse(screen,BALL_COLOR, ball)
    
    pygame.display.flip()
    clock.tick(60)
    
    
pygame.quit()
sys.exit()
