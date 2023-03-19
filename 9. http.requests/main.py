from pprint import pprint
from superhero import SuperheroAPI
from superhero import Superhero

def get_smartest_heroes():
    superhero_api = SuperheroAPI()
    data = superhero_api.get_all_superheroes()

    hulk = Superhero("Hulk", 0)
    captain_america = Superhero("Captain America", 0)
    thanos = Superhero("Thanos", 0)

    for hero_data in data:
        hero = Superhero.superheroes_dict(hero_data)
        if hero.name == "Hulk":
            hulk = hero
        elif hero.name == "Captain America":
            captain_america = hero
        elif hero.name == "Thanos":
            thanos = hero

    smartest = max([hulk, captain_america, thanos], key=lambda hero: hero.intelligence)
    return (f"Cамым умным супергероем является {smartest}")

if __name__ == '__main__':
    print(get_smartest_heroes())