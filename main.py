import requests
import random
import webbrowser

# Funcion para checar que token o login funciona
def check_login():

    url = "https://api.themoviedb.org/3/authentication"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzM2IxOWI4Y2Y0Nzg1YWQyMjQ1MDQ2Y2Q0MjIwYmNjYSIsInN1YiI6IjY2MzE5ZjNlODEzY2I2MDEyOTg2MjU2ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zdZ2Pu1sxaZZd3qWr1WcZwV8OJ02986rMyR81Ebx-8Y"
    }

    response = requests.get(url, headers=headers)

    print(response.text)
    

def obtener_peliculas(page, puntuacion, generos):
    

    url = "https://api.themoviedb.org/3/discover/movie"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzM2IxOWI4Y2Y0Nzg1YWQyMjQ1MDQ2Y2Q0MjIwYmNjYSIsInN1YiI6IjY2MzE5ZjNlODEzY2I2MDEyOTg2MjU2ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zdZ2Pu1sxaZZd3qWr1WcZwV8OJ02986rMyR81Ebx-8Y"
    }

    params = {
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": page,
        "vote_average.gte": puntuacion,
        "with_genres": generos
    }

    response = requests.get(url, headers=headers, params=params)

    return response.json()['results']

while True:
    print("""
selecciona una opción:
1) Checar el token
2) Obtener una lista de peliculas
3) Obtener una película
n) Salir
""")
    opcion = int(input('> '))
    match opcion:
        case 1:
            check_login()
        case 2:
            lista_peliculas = obtener_peliculas(1, 6, [28])
            print('---------- Lista de películas -------------')
            print(obtener_peliculas)
            print('-------------------------------------------')
        case 3:
            # Le pedimos a l usuario la página del catálogo de peliculas
            pagina_del_catalogo = int(input('Ingresa la página del catálogo: '))
            # Le pedimos el puntaje promedio
            puntaje_promedio = float(input('Ingresa el puntaje promedio de la pelicula: '))
            # Le pedimos las categorias
            categorias = input('Ingresa categorías separadas por coma: ')
            # Separamos el string de categorias y lo convertimos en una lista
            categorias = categorias.split(',')
            # Obtenemos las peliculas
            lista_de_pelis = obtener_peliculas(pagina_del_catalogo, puntaje_promedio, categorias)
            pelicula_aleatoria = random.choice(lista_de_pelis)
            print(pelicula_aleatoria)
            print('---------------- Película -----------------')
            print(f"Título {pelicula_aleatoria['original_title']}")
            print(f"Puntaje: {pelicula_aleatoria['vote_average']}")
            print(f"Poster: {pelicula_aleatoria['poster_path']}")
            print('-------------------------------------------')
        case "n":
            break
        case _:
            print('Esa opción no existe:(')
        
    