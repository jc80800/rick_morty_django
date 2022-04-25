import requests

BASE_URL = "https://rickandmortyapi.com/api"

def get_all_characters(page_num):
    response = requests.get(BASE_URL + '/character/' + "?page=" + str(page_num))
    if response.status_code == 200:
        response = response.json()
        character_lst = []
        num_pages = response['info']['pages']
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
        information = {
            'character_lst' : character_lst,
            'num_pages' : num_pages
        }
        return information
        
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
                    'episode' : episode_response['episode'],
                    'id' : episode_response['id']
                }
                episode_detail.append(detail)
            else:
                print(episode_response.status_code)
        response['episode'] = episode_detail
        return response
    else:
        print(response)

def get_all_episodes():
    response = requests.get(BASE_URL + "/episode")

    if response.status_code == 200:
        response = response.json()

        results = response['results']
        episode_detail = []
        for episode in results:
            detail = {
                'id' : episode['id'],
                'name' : episode['name'],
                'air_date' : episode['air_date'],
                'episode' : episode['episode']
            }
            episode_detail.append(detail)
        return episode_detail
    else:
        print(response.status_code)

def get_one_episode(id):
    response = requests.get(BASE_URL + "/episode/" + str(id))

    if response.status_code == 200:
        episode = response.json()
        detail = {
            'id' : episode['id'],
            'name' : episode['name'],
            'air_date' : episode['air_date'],
            'episode' : episode['episode']
        }
        return detail
    else:
        print(response.status_code)


    
