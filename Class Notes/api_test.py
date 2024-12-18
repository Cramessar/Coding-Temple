import requests
import json

# Function to fetch data from PokeAPI for a single Pokémon
def fetch_single_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)    

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()  # Convert response to Python dictionary
        abilities = data["abilities"]

        print(f"\n{pokemon_name.capitalize()} Abilities:")
        for ability in abilities:
            print(f"Name: {ability['ability']['name']}\n"
                  f"URL: {ability['ability']['url']}\n")
        
        return data
    else:
        print(f"Failed to fetch data for {pokemon_name}. Status code: {response.status_code}")
        return None

# Fetch data for Pikachu
fetch_single_pokemon("pikachu")
