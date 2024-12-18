import requests
import json

# Function to fetch data from PokeAPI for a single Pokémon
def fetch_pokemon(pokemons):
    url = f" https://pokeapi.co/api/v2/pokemon?limit=6&offset=0"
    response = requests.get(url)    

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()  # Convert response to Python dictionary
        forms = data["results"]
        #print(forms)
        # print(f"\n{results} forms:")
        for result in forms:
             print(f"Name: {result['name']}\n"
                  f"URL: {result['url']}\n")
        # return data
    else:
        print(f"Failed to fetch data for {pokemon_name}. Status code: {response.status_code}")
        return None

fetch_pokemon("")

