import cv2
import os
import datetime
import time

#Creamos una carpeta done guardaremos todas las fotos
carpeta_fotos = "fotos_sonrisas"
if not os.path.exists(carpeta_fotos):
    os.makedirs(carpeta_fotos)
    
def tomar_foto(sonrisas, carpeta_fotos):
    if(len(sonrisas) > 0):
        # Creamos el nombre de nuestro archivo
        nombre_archivo = datetime.datetime.now().strftime('%Y%m%d_%H%M%S.jpg')
        
        # Le decimos a python que meta ese archivo en la carpeta que le indiquemos
        ruta_completa = os.path.join(carpeta_fotos, nombre_archivo)
        
        #Tomamos una foto con opencv de lo que está viendo la cámara y la guardamos en la carpeta
        cv2.imwrite(ruta_completa, frame)
        
        # Damos la indicación que se tomó la foto
        print(f'Foto guardada como {ruta_completa}')
        

        
       

# Cargamos el clasificador de caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargamos el clasificador de ojos
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml' )

# Cargamos el clasificador de sonrisas
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')


captura = cv2.VideoCapture(0)

retenido, frame = captura.read()

while True:
    
    # Retenemos el frame que está viendo la cámara
    retenido, frame = captura.read()
    
    mi_imagen_bn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
  
    
    #print(mi_imagen_bn)
    
    
    mi_cara = face_cascade.detectMultiScale(mi_imagen_bn, 1.1, 2)

    #print(mi_cara)
    
    for (x, y, w, h) in mi_cara:
        
        #Función que se encarga de dibujar un rectangulo en mi cara
        # Primer parametro: Donde lo va a dibujar
        # Segundo parametro: La posición en X y Y donde se estará dibujando el cuadrado
        # Tercer parametro: El tamaño de los lados en mi rectangulo
        # Cuarto parametro: El color en RGB que tendrá mi rectangulo
        # Quinto parametro: El grosor de los dados
        cv2.rectangle(frame, (x, y), (x+w, y+h), (176, 2, 250), 2)
        
        # Creamos una región de interes
        region_cara = frame[y:y+h, x:x+w]
        # Creamos una región de la cara pero en blanco y negro
        region_cara_bn = mi_imagen_bn[y:y+h, x:x+w]
        
        # Creamos el método con el cual se hace la detección de mis ojos (regresa una matriz)
        ojos = eye_cascade.detectMultiScale(region_cara_bn, 1.2,2)
        
        #Creamos el método para detectar sonrisa (regresa una matriz)
        sonrisa = smile_cascade.detectMultiScale(region_cara_bn, 1.8, 20)
        
        """
        # Recorrer esa matriz para hayar la posición (en X y Y) de mis ojos, asi como su tamaño
        for (ex, ey, ew, eh) in ojos:
            # dibujamos rectangulos en los ojos
            cv2.rectangle(region_cara, (ex, ey), (ex + ew, ey + eh), (0,255,0), 2)
            """
            
        # Recorrer la matriz de la sonrisa para hayar la posición en X y Y, y su tamaño
        for (sx, sy, sw, sh) in sonrisa:
            # dibujamos rectangulos en los ojos
            cv2.rectangle(region_cara, (sx, sy), (sx + sw, sy + sh), (0,0,255), 2)
            tomar_foto(sonrisa, carpeta_fotos)
            time.sleep(.3)

            

 
    # Mostar en tiempo real lo que esta detectando opencv
    cv2.imshow('Mi detector', frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la captura y destruye todas las ventanas cuando termines
captura.release()
cv2.destroyAllWindows()