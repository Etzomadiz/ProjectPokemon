#This class is for pokemon attacks. Need to figure out stat lowering moves as well as priority modifiers
class Move:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
#Basic class for pokemon. Still need to add other things like traits and stats like speed etc.
class Pokemon:
    def __init__(self, name, type, hp, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.moves = moves

class PokemonBox:
    def __init__(self):
        self.pokemon = []

    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)

#This class handles the pokemon team and has some basic features like adding and removing pokemon
#it also can swap pokemon with the box when that feature finally gets added.
class PokemonTeam:
    def __init__(self):
        self.team = []

    def add_pokemon(self, pokemon):
        if len(self.team) < 6:
            self.team.append(pokemon)
        else:
            print("Cannot add more than 6 Pokémon to the team.")

    def remove_pokemon(self, pokemon):
        if pokemon in self.team:
            self.team.remove(pokemon)
        else:
            print("Pokémon not found in the team.")

    def swap_pokemon_with_box(self, pokemon_box, pokemon_to_swap):
        if len(self.team) > 0:
            # Add the chosen Pokémon from the team to the box
            pokemon_box.add_pokemon(pokemon_to_swap)
            self.remove_pokemon(pokemon_to_swap)
            # Add a Pokémon from the box to the team if there's space
            if len(pokemon_box.pokemon) > 0:
                pokemon_to_add = pokemon_box.pokemon.pop(0)
                self.add_pokemon(pokemon_to_add)
        else:
            print("Cannot swap Pokémon. The team is empty.")


#started with 4 moves for pikachu for test purposes. Will eventually need to create a csv file with moves and pokemon type to fill later.
thunder = Move("Thunder", 80, "Electric")
quickAttack = Move("Quick Attack", 40, "Eletric")
ironTail = Move("Iron Tail", 60, "Steel")
static = Move("Static", 0, "Electric" )

#created first pokemon for testing purposes
pikachu = Pokemon("Pikachu", "Electric", 100, {thunder, quickAttack, ironTail, static})

mainTeam = PokemonTeam()
pokeBox = PokemonBox()

mainTeam.add_pokemon(pikachu)

#proof of concept for calling pokemon namaes and potentially editing pokemon things like hp
#also will need to figure out some sort of level system for the pokemon
x = -1
while(x != 0):
    print("------------------------------------------------------")
    print("Choose one of the following options:")
    print("1. Search for a random encounter.")
    print("2. Make your first pokemon take 20 damage.")
    print("3. Display the information from your first pokemon.")
    print("0. Exit the Program")
    print("------------------------------------------------------")
    userInput = int(input("Type Number to make a choice: "))
    if(userInput == 1):
        print("Something for now")
    elif(userInput == 2):
        mainTeam.team[0].hp -= 20
    elif(userInput == 3):
        print(mainTeam.team[0].name)
        print("Type: " + mainTeam.team[0].type)
        print("The pokemon has: " + str(mainTeam.team[0].hp) + " HP")
    elif(userInput == 0):
        print("Thankyou for playing")
        x = 0
    else:
        print("Not a valid option try again....")
    