class Move:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type

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



thunder = Move("Thunder", 80, "Electric")
quickAttack = Move("Quick Attack", 40, "Eletric")
ironTail = Move("Iron Tail", 60, "Steel")
static = Move("Static", 0, "Electric" )

pikachu = Pokemon("Pikachu", "Electric", 100, {thunder, quickAttack, ironTail, static})

mainTeam = PokemonTeam()
pokeBox = PokemonBox()

mainTeam.add_pokemon(pikachu)

print(mainTeam.team[0].name)
print("Type: " + mainTeam.team[0].type)
print("The pokemon has: " + str(mainTeam.team[0].hp) + " HP")