import requests
import random
import webbrowser

    # Headers para la API
headers = {
    "accept": "application/json",
    "Authorization": "Bearer ..."
}
    


# Función para verificar que nuestro TOKEN funciona
def check_login():

    # Url de la API para verificar la autenticación
    url = "https://api.themoviedb.org/3/authentication"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzM2IxOWI4Y2Y0Nzg1YWQyMjQ1MDQ2Y2Q0MjIwYmNjYSIsInN1YiI6IjY2MzE5ZjNlODEzY2I2MDEyOTg2MjU2ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zdZ2Pu1sxaZZd3qWr1WcZwV8OJ02986rMyR81Ebx-8Y"
    }
    
    # Obtenemos una respuesta
    response = requests.get(url, headers=headers)

    # Imprimimos la respuesta
    print(response.text)


# Función para obtener una lista de películas con base en cierto parámetros
def obtener_peliculas(page, puntuacion, generos):
    
    # Ruta para descubrir películas
    url = "https://api.themoviedb.org/3/discover/movie"
    
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzM2IxOWI4Y2Y0Nzg1YWQyMjQ1MDQ2Y2Q0MjIwYmNjYSIsInN1YiI6IjY2MzE5ZjNlODEzY2I2MDEyOTg2MjU2ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zdZ2Pu1sxaZZd3qWr1WcZwV8OJ02986rMyR81Ebx-8Y"
    }

    # Parámetros para la petición
    params = {
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": page,
        "vote_average.gte": puntuacion,
        "with_genres": generos   
    }

    # Obtenemos respuesta
    response = requests.get(url, headers=headers, params=params)

    # Retornamos la lista de pelis
    return response.json()['results']


def open_web_browser(link):
    webbrowser.open_new_tab(link)


def search_streaming(movie_id):
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"
    
    servicios = requests.get(url, headers=headers)
    return servicios.json()['results']


while True:
    
    print("""

Selecciona una opción:
1) Checar el Token
2) Obtener una lista de peliculas
3) Obtener una película aleatoria
4) Abrir link secreto :o


n) Salir

""")
    opcion = input('> ')
    
    match opcion:
        case "1":
            check_login()
        case "2":
            
            obtener_peliculas = obtener_peliculas(1, 6, [28])
            print('---------- Lista de películas ---------')
            print(obtener_peliculas)
            print('---------------------------------------')
       
       
        case "3":
            
            poster_url = 'https://image.tmdb.org/t/p/w500'
    
            # Le pedimos al usuaria la página del catalogo de pelis
            pagina_del_catalogo = int(input('Ingresa la página del catalogo: '))

            # Le pedimos el puntaje promedio
            puntaje_promedio = float(input('Ingresa el puntaje promedio de la peli: '))

            # Le pedimos las categorias
            categorias = input('Ingresa categorías separadas por coma: ')

            # Separamos el string de categorias y lo convertimos en una lista
            categorias = categorias.split(',')

            # Obtenemos las peliculas
            lista_de_pelis = obtener_peliculas(pagina_del_catalogo, puntaje_promedio, categorias)

            # Hacemos una selección aleatoria de una peli
            pelicula_aleatoria = random.choice(lista_de_pelis)
            # Imprimos el resultado
            print('---------- Película ---------')
            print(f"ID: {pelicula_aleatoria['id']}")
            print(f"Título: {pelicula_aleatoria['original_title']}")
            print(f"Puntaje: {pelicula_aleatoria['vote_average']}")
            print(f"Poster: {poster_url + pelicula_aleatoria['poster_path']}")
            print('---------------------------------------')
            
            diccionario_streaming = search_streaming(pelicula_aleatoria['id'])
            
            open_web_browser(poster_url + pelicula_aleatoria['poster_path'])
            
       
            for llave, valor in diccionario_streaming:
               print(f'{llave}: {valor}')
       
        case "4":
            open_web_browser('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            
        case "5":
            resultados_streaming = search_streaming(123)
            for valor in resultados_streaming.values():
                print(valor)
            
        case "n":
            break
        
        case _:
            print('Esa opción no existe :(')