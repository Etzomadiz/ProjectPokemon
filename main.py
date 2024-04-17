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

class PokemonTeam:
    def __init__(self):
        self.team = []

    def add_pokemon(self, pokemon):
        if len(self.team) < 6:
            self.team.append(pokemon)
        else:
            print("Cannot add more than 6 Pokémon to the team.")


thunder = Move("Thunder", 80, "Electric")
quickAttack = Move("Quick Attack", 40, "Eletric")
ironTail = Move("Iron Tail", 60, "Steel")
static = Move("Static", 0, "Electric" )

pikachu = Pokemon("Pikachu", "Electric", 100, {thunder, quickAttack, ironTail, static})

