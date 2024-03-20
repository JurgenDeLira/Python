from pynput.keyboard import Key, Listener

def onPress(key):
        print(f'Se pulso una tecla {key}')
    
def onRelease(key):
        print(f'Se dejo de presionar una tecla{key}')

# Creamos un método que aprovecha las dos funcunciones que 
# hicimos y los renombramos 'listener'

with Listener(on_press = onPress, on_release = onRelease) as listener:
  # Le indicamos al método que todas las pulsaciones las va a detectar
  listener.join()