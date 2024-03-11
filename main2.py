import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

captura = cv2.VideoCapture(0)

retenido, frame = captura.read()

while True:
    retenido, frame = captura.read()
    
    mi_imagen_bn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #print(mi_imagen_bn)
    
    
    mi_cara = face_cascade.detectMultiScale(mi_imagen_bn, 1.1, 2)

    print(mi_cara)
    
    """for (x, y, w, h) in mi_cara:
        print(x)""" #Para detectarlo en X
    
    #Mostrar en tiempo real lo que esta detectando opencv
    cv2.imshow('Mi detector', frame) #ponle mi_imagen_bn para en blanco y negro

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera la captura y destruye todas las ventanas cuando termines
captura.release()
cv2.destroyAllWindows()