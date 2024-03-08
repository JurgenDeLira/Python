import cv2

#Va a almacenar de la libreria cv2 el metodo siguiente, que es el que sirve para leer caras:
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     'haarcascade_frontalface_default.xml')
#haarcascade es el archivo con el que vamos a entrenar nuestra camara para que detecte rostros

captura = cv2.VideoCapture(0) # El 0 es para conectarse a la primer camara disponible

while True:
    retenido, frame = captura.read()
    
    print(frame)
