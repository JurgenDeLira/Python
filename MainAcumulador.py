from pynput.keyboard import Key, Listener

teclas_presionadas = []

def onPress(key):
    if key == Key.esc:
        return None
    elif key == Key.space:
        teclas_presionadas.append('_')
    else:
        print(f'Se pulso una tecla {key}')
        teclas_presionadas.append(key)
    
def onRelease(key):
    if key == Key.esc:
        return None
    print(teclas_presionadas)

# Creamos un método que aprovecha las dos funcunciones que 
# hicimos y los renombramos 'listener'

with Listener(on_press = onPress, on_release = onRelease) as listener:
  # Le indicamos al método que todas las pulsaciones las va a detectar
  listener.join()