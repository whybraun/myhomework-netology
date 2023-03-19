import requests

class SuperheroAPI:
    def __init__(self):
        self.url = "https://akabab.github.io/superhero-api/api/all.json"
        
    def get_all_superheroes(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

class Superhero:
    def __init__(self, name, intelligence):
        self.name = name
        self.intelligence = intelligence

    def __str__(self):
        return f"{self.name} ({self.intelligence})"

    @classmethod
    def superheroes_dict(cls, data):
        name = data.get("name")
        intelligence = int(data.get("powerstats", {}).get("intelligence", 0))
        return cls(name, intelligence)

