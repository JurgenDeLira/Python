```python
import cv2
import os
import datetime
import time

# Creamos una carpeta donde guardaremos todas las fotos
carpeta_fotos = "fotos_sonrisas"
if not os.path.exists(carpeta_fotos):
    os.makedirs(carpeta_fotos)
    

def overlay_imagen(background, overlay, position=(0,0)):
    """
    Superpone una imagen con transparencia (overlay) sobre una imagen de fondo (background) en una posición dada.
    :param background: Imagen de fondo sobre la cual superponer.
    :param overlay: Imagen PNG con transparencia para superponer.
    :param position: Una tupla (x, y) que representa la posición superior izquierda donde se superpondrá la imagen.
    """
    
    # Extraemos las dimensiones  y la opacidad de la imagen
    overlay_height, overlay_width = overlay.shape[:2]
    overlay_alpha = overlay[:,:,3] /255
    
    # Calcular donde se va a superponer la imagen y la opacidad del fondo
    x,y = position
    background_alpha = 1.0 - overlay_alpha
    
    # Calculamos el espacio para el canal RGB:
    for color in range(0,3):
        # Hacemos la conversión del canal Alfa al canal RGB: 
        background[y:y+overlay_height, x:x+overlay_width, color] = (overlay_alpha * overlay[:,:,color] + background_alpha * background[y:y+overlay_height, x:x+overlay_width, color])
        
    
    return background    


def timer_asincrono():
    global tiempo_anterior
   # Supongamos que este es el momento específico del que queremos calcular la diferencia
    tiempo_actual = datetime.datetime.now()

    diferencia = tiempo_actual - tiempo_anterior
    
    # Verificar si han pasado dos segundos o más
    if diferencia >= datetime.timedelta(seconds=2):
        print("Han pasado 2 segundos o más.")
        # Actualizar el "tiempo anterior" con el tiempo actual
        tiempo_anterior = tiempo_actual
        return True
    
    return False

def tomar_foto(sonrisas, carpeta_fotos):
    if(len(sonrisas) > 0):
        # Creamos el nombre de nuestro archivo
        nombre_archivo = datetime.datetime.now().strftime('%Y%m%d_%H%M%S.jpg')
        
        # Le decimos a python que meta ese archivo en la carpeta que le indiquemos
        ruta_completa = os.path.join(carpeta_fotos, nombre_archivo)
        
        # Tomamos una foto con opencv de lo que está viendo la cámara y la guardamos en la carpeta
        cv2.imwrite(ruta_completa, frame)
        
        # Damos la indicación que se tomó la foto
        print(f'Foto guardada como {ruta_completa}')
        

# Cargamos el clasificador de caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargamos el clasificador de sonrisas
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')



captura = cv2.VideoCapture(0)

retenido, frame = captura.read()

tiempo_anterior = datetime.datetime.now()

while True:
    
    # Retenemos el frame que está viendo la cámara
    retenido, frame = captura.read()
    
    mi_imagen_bn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    mi_cara = face_cascade.detectMultiScale(mi_imagen_bn, 1.1, 2)
    
    for (x, y, w, h) in mi_cara:
        
        sombrero = cv2.imread('sombrero.png', -1)
        
        sombrero = cv2.resize(sombrero, (w, h)) # Ajustamos la imagen a lo que necesitamos
        overlay_imagen(frame, sombrero, (x, y - int(h/2)))
        
        #Función que se encarga de dibujar un rectangulo en mi cara
        # Primer parametro: Donde lo va a dibujar
        # Segundo parametro: La posición en X y Y donde se estará dibujando el cuadrado
        # Tercer parametro: El tamaño de los lados en mi rectangulo
        # Cuarto parametro: El color en RGB que tendrá mi rectangulo
        # Quinto parametro: El grosor de los dados
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (176, 2, 250), 2)
        
        # Creamos una región de interes
        region_cara = frame[y:y+h, x:x+w]
        
        # Creamos una región de la cara pero solo en blanco y negro
        region_cara_bn = mi_imagen_bn[y:y+h, x:x+w]
        
        # Creamos el método con el cual se hace la deteción de la sonrisa (regresa una matríz)
        sonrisa = smile_cascade.detectMultiScale(region_cara_bn, 1.8, 20)
                
        # Recorrer la matríz de la sonrisa para hayar la posión en X y Y, y también su tamaño    
        for (sx, sy, sw, sh) in sonrisa:
            # Dibujamos un rectangulo en la sonrisa
            #cv2.rectangle(region_cara, (sx, sy), (sx + sw, sy + sh), (0,0,255), 2)
            if timer_asincrono():
                tomar_foto(sonrisa, carpeta_fotos)
                
    
    # Mostar en tiempo real lo que esta detectando opencv
    cv2.imshow('Mi detector', frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la captura y destruye todas las ventanas cuando termines
captura.release()
cv2.destroyAllWindows()
```