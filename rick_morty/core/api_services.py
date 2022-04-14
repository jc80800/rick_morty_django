import requests

BASE_URL = "https://rickandmortyapi.com/api"

def get_all_characters():
    response = requests.get(BASE_URL + '/character')
    if response.status_code == 200:
        response = response.json()
        character_lst = []
        results = response['results']
        for item in results:
            character = {
                'id' : item['id'],
                'name' : item['name'],
                'image': item['image'],
                'status': item['status'],
                'species': item['species'],
            }
            character_lst.append(character)
        return character_lst
    else:
        print(response)
    