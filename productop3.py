import requests
from tabulate import tabulate

# Función para obtener todos los personajes
def get_all_characters():
    all_characters = []
    page = 1
    while page < 12:  # Actualizar el número total de páginas según la paginación de la API
        characters_response = requests.get(f'https://api.attackontitanapi.com/characters?page={page}')
        if characters_response.status_code == 200:
            characters_data = characters_response.json()
            results = characters_data['results']
            all_characters.extend(results)
            page += 1
        else:
            print(f'Error al obtener los datos de la página {page} de la API de personajes:', characters_response.status_code)
            return None
    return all_characters

# Función para mostrar los personajes en forma de tabla
def show_characters_table(characters):
    table_data = []
    for character in characters:
        table_data.append([character['id'], character['name'], character['gender'], character['age'], character['status']])
    headers = ["ID", "Name", "Gender", "Age", "Status"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Función para buscar un personaje por nombre
def search_character(characters):
    while True:
        search_name = input("¿Deseas buscar un personaje por nombre? (s/n): ")
        if search_name.lower() == 's':
            name_to_search = input("Ingresa el nombre del personaje que quieres buscar: ")
            search_results = [character for character in characters if name_to_search.lower() in character['name'].lower()]
            if search_results:
                print("\nResultados de la búsqueda:")
                search_table_data = [[character['id'], character['name'], character['gender'], character['age'], character['status']] for character in search_results]
                print(tabulate(search_table_data, headers=["ID", "Name", "Gender", "Age", "Status"], tablefmt="grid"))
            else:
                print("\nNo se encontraron resultados para el nombre ingresado.")
        else:
            break

# Obtener todos los personajes
all_characters = get_all_characters()
if all_characters:
    show_characters_table(all_characters)
    search_character(all_characters)
