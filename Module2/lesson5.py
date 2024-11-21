#lesson 5
import re


# Function to write TV shows to a file
def write_show(shows):
    with open('shows_list.txt', 'w') as file:
        for show in shows:
            file.write(f"{show['Title']}-:-{show['Platform']}-:-{show['Genre']}\n")

# Function to read TV shows from a file
def read_shows():
    shows_list = []
    with open('shows_list.txt', 'r') as file:
        for line in file:
            data = re.search(r"([\w\s]+)-:-([\w\s]+)-:-([\w\s]+)", line)
            shows_list.append({'Title': data.group(1), 'Platform': data.group(2), 'Genre': data.group(3).strip()})
    return shows_list

# Main function to run the TV show manager
def main():
    while True:
        shows_list = read_shows()  # Read the current list of shows from the file
        action = input('''
Options
-----------------------
1 - Add a TV Show
2 - Remove a TV Show
3 - View List of TV Shows
4 - Quit
''')
        if action == '1':
            add_show(shows_list)  # Add a new show
        elif action == '2':
            remove_show(shows_list)  # Remove a show
        elif action == '3':
            view(shows_list)  # View the list of shows
        elif action == '4':
            print("Thanks for using this app!")
            break

main()