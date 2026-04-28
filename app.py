import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
""" print(data[0]) """

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
""" for index, pokemon in data:
    print(index, ":", pokemon["name"]) """
# Add a language choice feature and print the pokemons name based on the user input
""" language_choice = input("Select a language: 1-japanese, 2-english, 3-chinese, 4-french: ")
for index, pokemon in data:
    if language_choice == "japanese":
            print(index, ":", pokemon["name"]["japanese"])
    elif language_choice == "english":
            print(index, ":", pokemon["name"]["english"])
    elif language_choice == "chinese":
            print(index, ":", pokemon["name"]["chinese"])
    elif language_choice == "french":
            print(index, ":", pokemon["name"]["french"]) """

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
""" for pokemon in data:
        print(pokemon["type"]) """
""" matches = [] """
pokemon_type = input("Choose a pokemon type: ")
for pokemon in data:
        if pokemon_type in pokemon["type"]:
                print(pokemon['name'])
                """ break """
else:
        print("No pokemon found of this type.")

""" if not matches:
        print("No pokemon found of this type.")
else:
        print(matches) """

"""     if pokemon['type'] != pokemon_type:
                print("No pokemon found of this type.")
        else:
                print(matches) """



#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
""" search_pokemon = input("Search for pokemon: ")
search = False """
search_pokemon = input("Search for pokemon: ")
for pokemon in data:
        if search_pokemon in pokemon["name"]["english"]:
                print(pokemon["name"])

else:
        print("No pokemon found with that name.")




#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type
#Based on user input, show all moves that pokemon could learn based on type. For example, if Charizard is fire/fyling, show all fire and flying moves.

