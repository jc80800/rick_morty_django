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
        print(response.status_code)

def get_character_detail(id):
    response = requests.get(BASE_URL + '/character/' + str(id))
    if response.status_code == 200:
        response = response.json()
        episode_detail = []
        episodes = response['episode']
        for episode in episodes:
            episode_response = requests.get(episode)
            if episode_response.status_code == 200:
                episode_response = episode_response.json()
                detail = {
                    'name' : episode_response['name'],
                    'air_date' : episode_response['air_date'],
                    'episode' : episode_response['episode']
                }
                episode_detail.append(detail)
            else:
                print(episode_response.status_code)
        response['episode'] = episode_detail
        return response
    else:
        print(response)
    
