# Nos permite pedir cosas desde internet
import requests
# Generador de estados aleatorios
import random
# Convetir  imagenes de base 64 a imagenes visibles
from io import BytesIO
# Manipular imágenes desde python
from PIL import Image, ImageFont, ImageDraw

# .get es un método
respuesta_api = requests.get("https://api.imgflip.com/get_memes")

lista_memes = respuesta_api.json()['data']['memes']

random_choice = random.choice(lista_memes)

imagen_meme = requests.get(random_choice['url'])

imagen = Image.open(BytesIO(imagen_meme.content))

font_size = 58
font = ImageFont.truetype('ComicNeue-Bold.ttf', size = font_size)

draw = ImageDraw.Draw(imagen)

text = "Soy un meme"

color = "White"

draw.text((50,100), text, font=font, fill=color)

imagen.show()