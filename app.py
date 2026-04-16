import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
""" print(data[0]) """

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
""" for index, pokemon in enumerate(data):
    print(index, ":", pokemon["name"]) """
# Add a language choice feature and print the pokemons name based on the user input
""" language_choice = input("Select a language: 1-japanese, 2-english, 3-chinese, 4-french: ")
if language_choice == "japanese":
    for index, pokemon in enumerate(data):
        print(index, ":", pokemon["name"]["japanese"])
elif language_choice == "english":
    for index, pokemon in enumerate(data):
        print(index, ":", pokemon["name"]["english"])
elif language_choice == "chinese":
    for index, pokemon in enumerate(data):
        print(index, ":", pokemon["name"]["chinese"])
elif language_choice == "french":
    for index, pokemon in data:
        print(index, ":", pokemon["name"]["french"]) """

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
pokemon_type = input("Choose a pokemon type: ")
if pokemon_type == "Normal":
    for index, pokemon in data:
        print(pokemon["type"]["normal"])
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
""" search_pokemon = input("Search for pokemon: ") """
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type

