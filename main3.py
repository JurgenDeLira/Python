import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

captura = cv2.VideoCapture(0)

retenido, frame = captura.read()

while True:
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
    
    # Mostar en tiempo real lo que esta detectando opencv
    cv2.imshow('Mi detector', frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la captura y destruye todas las ventanas cuando termines
captura.release()
cv2.destroyAllWindows()
