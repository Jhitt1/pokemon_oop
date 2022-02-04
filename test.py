from pip._vendor import requests
type_poke = f"https://pokeapi.co/api/v2/type/{class_type}{charecters}{abilities}{statistics}/"
chosen_poke_type = requests.get(type_poke).json()
pass
api_link = f'https://pokeapi.co/api/v2/pokemon/{4}/'
self.data = requests.get(api_link).json()
