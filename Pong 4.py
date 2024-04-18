import pygame # Librería principal
import sys # Manipular cosas básicas del OS
import random # Generar valores aleatorios






# Inicializar la librería pygame
pygame.init()

# Si el nombre de la variable está en MAYÚSCULAS es constante


# Define el alto de la pantalla
PANTALLA_ALTO = 600

# Define el largo de la pantalla
PANTALLA_LARGO = 800

# Define el color de fondo
BACKGROUND_COLOR = (43, 43, 43)

# Definimos el color de las raquetas
PADDLE_COLOR = (255, 255, 255)

# Velocidad de las raquetas
PADDLE_SPEED = 5

# Define el color de la pelota
BALL_COLOR = (255, 255, 255)


# Rapidez de la pelota
BALL_SPEED = [5,5]

#Fuente del texto
font = pygame.font.Font(None, 140)

FONT_COLOR = (255, 255, 255)

#Puntuación PC
computer_score = 0
#Puntuación player
player_score = 0

# Se guarda la pantalla
screen = pygame.display.set_mode((PANTALLA_LARGO, PANTALLA_ALTO))

# Se guarda la pelota
ball = pygame.Rect(PANTALLA_LARGO // 2, PANTALLA_ALTO // 2, 20, 20)


# Se crea la raqueta         # Posición en X        Posición en Y

player_paddle = pygame.Rect(PANTALLA_LARGO - 20, PANTALLA_ALTO // 2, 10, 100)

computer_paddle = pygame.Rect(10, PANTALLA_ALTO // 2, 10, 100)




# Variable que contrendrá el reloj interno del juego
clock = pygame.time.Clock()

# Función para darle movimiento a la paleta del jugador
def move_player_paddle():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
        
        
    elif keys[pygame.K_s] and player_paddle.bottom < PANTALLA_ALTO:
        
        player_paddle.y += PADDLE_SPEED
        

def move_computer_paddle():
    if random.randint(0, 10) < 9:
    
        if computer_paddle.centery < ball.centery:
            computer_paddle.y += PADDLE_SPEED
        else:
            computer_paddle.y -= PADDLE_SPEED
        
    #Delimitar que no se salga de la pantalla el computerpaddle
    if computer_paddle.top <= 0:
        computer_paddle.top = 0
    if computer_paddle.bottom >= PANTALLA_ALTO:
        computer_paddle.bottom = PANTALLA_ALTO
  


# Función para que la pelota se mueva
def ball_move():
    global player_score
    global computer_score
    
    ball.x += BALL_SPEED[0]
    ball.y += BALL_SPEED[1]
    
    
    if ball.top <= 0 or ball.bottom >= PANTALLA_ALTO:
        BALL_SPEED[1] = -BALL_SPEED[1]
    
    #Esta condicional determina si la pelota salio de la pantalla
        
    #Si se sale de lado izquierdo
    if ball.left <= 0 :
        player_score += 1
        ball.x = PANTALLA_LARGO // 2
        ball.y = PANTALLA_ALTO // 2
        
    #Si se sale de lado derecho
    if ball.right >= PANTALLA_LARGO:
        computer_score += 1
        ball.x = PANTALLA_LARGO // 2
        ball.y = PANTALLA_ALTO // 2
        
        
        
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        BALL_SPEED[0] = -BALL_SPEED[0]


# Varaible que definirá el estado de mi juego
running = True

# Bucle principal del juego
while running:
    
    
    # Detectar las teclas que el usuario presionó
    for event in pygame.event.get():
        
        # Si se presiona el botón de "exit" se sale del juego y cierra la ventana
        if event.type == pygame.QUIT:
            running = False
    
    # Llamar la clase ball_move()
    ball_move()
    
    # Llamar la función move_player_paddle()
    move_player_paddle()
    
    # Llamar la función move_computer_paddle()
    move_computer_paddle()
    
    #Se renderiza la fuente con el puntaje de mi jugador
    player_text = font.render(str(player_score), True, FONT_COLOR)
    
    #Se renderiza la fuente con el puntaje de mi computador
    computer_text = font.render(str(computer_score), True, FONT_COLOR)
    
    
            
    # Rellenamos nuestra pantalla de algún color
    screen.fill(BACKGROUND_COLOR)
    
    #Dibujamos las raquetas
    pygame.draw.rect(screen, PADDLE_COLOR, player_paddle)
    pygame.draw.rect(screen, PADDLE_COLOR, computer_paddle)
    
    #Dibujar la pelota
    pygame.draw.ellipse(screen, BALL_COLOR, ball)
    
    # Se va a dibujar el marcador
    # Se dibuja el marcador de mi usuario
    screen.blit(player_text, (PANTALLA_LARGO - 200, 50))
    # Se dibuja el marcador de la pc
    screen.blit(computer_text, (200,50))
    
    # Actualizabamos la pantalla
    pygame.display.flip()
    
    clock.tick(60) # Se ejecute en 60 fps (Frames Per Second)
    
    
# Cerramos el juego  
pygame.quit()
sys.exit()
    