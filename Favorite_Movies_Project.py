#Probably overkill for something simple, but I was feeling lazy when asked to enter the director.
#I wasnt sure what would happen if more than one movie shared the same name so I figured showing the movie poster might be a good idea.
#also I didnt want to create too many dependiencies like being able to navigate an app with pyqt or using something web based with flask so I thought this might be easy enough to use.

import requests
import webbrowser
from PIL import Image #requires pillow, pip install pillow in terminal
from io import BytesIO

movies = {}

def fetch_movie_data(title):
    api_key = "d549d0ec"  # Replace with your API key from IMDB, https://www.omdbapi.com/apikey.aspx
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['Response'] == 'True':
            return {
                'genre': data.get('Genre', 'N/A'),
                'rating': data.get('Rated', 'N/A'),
                'director': data.get('Director', 'N/A'),
                'year': data.get('Year', 'N/A'),
                'poster': data.get('Poster', None)
            }
        else:
            print(f"Movie '{title}' not found in OMDb API.\n")
            return None
    else:
        print("Error fetching movie data. Please try again.\n")
        return None


def show_poster(poster_url):
    if poster_url:
        response = requests.get(poster_url)
        img = Image.open(BytesIO(response.content))  
        img.show()  
    else:
        print("No poster available.")


def add_movie():
    title = input("Enter the movie title: ").strip()
    movie_data = fetch_movie_data(title)
    
    if movie_data:
        movies[title] = movie_data
        print(f"\n'{title}' has been added to your movie list.\n")
        # Shows the poster, didnt want to sped too much time figuring sizing issues because its small so my bad for that. 
        show_poster(movie_data['poster'])


def remove_movie():
    title = input("Enter the title of the movie you want to remove: ").strip()
    if title in movies:
        del movies[title]
        print(f"\n'{title}' has been removed from your movie list.\n")
    else:
        print(f"\nMovie '{title}' not found in your list.\n")


def display_movies():
    if movies:
        print("\nYour movie list:")
        for title, details in movies.items():
            print(f"\nTitle: {title}\nGenre: {details['genre']}\nRating: {details['rating']}\nDirector: {details['director']}\nYear: {details['year']}")
            if details['poster']:
                print(f"Poster URL: {details['poster']}")
    else:
        print("\nYour movie list is currently empty.\n")


def show_menu():
    print("\nMenu:")
    print("1. Add a movie")
    print("2. Remove a movie")
    print("3. View movie list")
    print("4. Quit")


def calc_input():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_movie()
        elif choice == '2':
            remove_movie()
        elif choice == '3':
            display_movies()
        elif choice == '4':
            print("\nExiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice, please try again.\n")


if __name__ == "__main__":
    calc_input()
