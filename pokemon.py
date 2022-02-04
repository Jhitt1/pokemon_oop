from pip._vendor import requests
type_poke = f"https://pokeapi.co/api/v2/type/{class_type}{charecters}{abilities}{statistics}/"
chosen_poke_type = requests.get(type_poke).json()
api_link = f'https://pokeapi.co/api/v2/pokemon/{4}/'
data = requests.get(api_link).json()



class class_type:
    @classmethod
    def _init_(self,):
        self.ground = f"https://pokeapi.co/api/v2/type/ground/"
        self.grass = f"https://pokeapi.co/api/v2/type/grass/"
        self.fire = f"https://pokeapi.co/api/v2/type/fire/"
        self.rock = f"https://pokeapi.co/api/v2/type/rock/"
        self.electric = f"https://pokeapi.co/api/v2/type/electric/"
        self.ghost = f"https://pokeapi.co/api/v2/type/ghost/"
        self.bug = f"https://pokeapi.co/api/v2/type/bug/"
        self.dragon = f"https://pokeapi.co/api/v2/type/dragon/"
        self.fairy = f"https://pokeapi.co/api/v2/type/fairy/"
        self.dark = f"https://pokeapi.co/api/v2/type/dark/"
        self.ice = f"https://pokeapi.co/api/v2/type/ice/"


    print(chosen_poke_type)

class Charecters:
    def _Init_(self, class_type):

        pass


class Abilities:
    pass


class statistics:
    pass
