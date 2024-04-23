import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pokemon shell')

# Load background image
background_image = pygame.image.load("pokegrass.png")
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

encounter_image = pygame.image.load("tallGrass.png")
encounter_image = pygame.transform.scale(encounter_image, (20,20))

battle_image = pygame.image.load("battleBack.png")
battle_image = pygame.transform.scale(battle_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Block parameters
BLOCK_SIZE = 10
block_x = (WINDOW_WIDTH - BLOCK_SIZE) // 2
block_y = (WINDOW_HEIGHT - BLOCK_SIZE) // 2
block_speed = 1  # Adjust this value to change the speed of movement

# Set up the clock
clock = pygame.time.Clock()
FPS = 60  # Frames per second

# Function to handle wild Pokémon encounter
def encounter_wild_pokemon():
    random_number = random.randint(1, 10)
    if random_number in [1, 4, 7]:
        print("A wild Pokémon appeared!")
        battleScenario = True
        window.blit(battle_image, (0, 0))
        
        while battleScenario: 
            pygame.display.flip()
    else:
        print("You did not find a Pokémon.")

# Define the encounter area within the background image
encounter_area_rect = pygame.Rect((WINDOW_WIDTH - encounter_image.get_width()) // 2,(WINDOW_HEIGHT - encounter_image.get_height()) // 2,encounter_image.get_width(),encounter_image.get_height())
encounter_area_rect.x = 20
encounter_area_rect.y = 20
# Flag to track encounter status
encounter_triggered = False

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the block based on WASD key inputs
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_a]:
        dx -= block_speed
    if keys[pygame.K_d]:
        dx += block_speed
    if keys[pygame.K_w]:
        dy -= block_speed
    if keys[pygame.K_s]:
        dy += block_speed

    # Allow movement in one direction at a time
    if dx != 0 and dy != 0:
        dx, dy = 0, 0

    # Update block position with the computed deltas
    block_x += dx
    block_y += dy

    # Ensure the block stays within the window boundaries
    block_x = max(0, min(WINDOW_WIDTH - BLOCK_SIZE, block_x))
    block_y = max(0, min(WINDOW_HEIGHT - BLOCK_SIZE, block_y))
    # Clear the screen with the background image
    window.blit(background_image, (0, 0))

    # Check for wild Pokémon encounter
    if encounter_area_rect.colliderect(pygame.Rect(block_x, block_y, BLOCK_SIZE, BLOCK_SIZE)):
        if not encounter_triggered:
            encounter_wild_pokemon()
            encounter_triggered = True
    else:
        encounter_triggered = False
    window.blit(encounter_image, (encounter_area_rect.x, encounter_area_rect.y))
    # Draw the block
    block_rect = pygame.Rect(block_x, block_y, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(window, RED, block_rect)

    

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()

class Move:
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
#Basic class for pokemon. Still need to add other things like traits and stats like speed etc.
class Pokemon:
    def __init__(self, name, type, level,hp, moves, speed):
        self.name = name
        self.type = type
        self.level = level
        self.hp = hp
        self.moves = moves
        self.speed = speed

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

def encounter_wild_pokemon():
    # List of wild Pokémon species
    random_number = random.randint(1, 10) #generates random number from 1-10
    if (random_number == 1 or random_number == 4 or random_number == 7):# checks if the random number generated is one of the success cases and if so intitates print stratement and returns the pokemon that was encountered.
        wild_pokemon_species = [pikachu]
        wild_pokemon_species = random.choice(wild_pokemon_species)
        print(f"A wild {wild_pokemon_species.name} appeared!")
        return wild_pokemon_species #If a pokemon is found then the value this function returns is the randomly generated pokemon.
    else:
        print("You did not find a pokemon.")
def battleSequence(pokemon):
    x = 1
    while(x != 0):
        print(pokemon.name)
        print("What would you like to do")
        print("1. fight")
        print("2. run")
        print("3. bag")
        print("4. Team")
        userInput = int(input("Type a number to choose."))
        if (userInput == 1):
            print("Somthing")
        elif(userInput == 2):
            print("Got away safely")
            x = 0
        elif(userInput == 3):
            print("Somthing else else")
        elif(userInput == 4):
            print("Something else else else")


#started with 4 moves for pikachu for test purposes. Will eventually need to create a csv file with moves and pokemon type to fill later.
thunder = Move("Thunder", 80, "Electric")
quickAttack = Move("Quick Attack", 40, "Eletric")
ironTail = Move("Iron Tail", 60, "Steel")
static = Move("Static", 0, "Electric" )

#created first pokemon for testing purposes
pikachu = Pokemon("Pikachu", "Electric",5, 100, {thunder, quickAttack, ironTail, static}, 19)

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
        randomEncounter = encounter_wild_pokemon()#this sets random encounter to the pokemon that is returned from the ecounter wild pokemon function.
        if (randomEncounter != None):
            battleSequence(randomEncounter)#battle sequence displays if a random encounter takes place. 
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