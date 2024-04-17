#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define MAX_MOVES 4
#define MAX_NAME_LENGTH 20


// Struct for representing a move
typedef struct {
    char name[MAX_NAME_LENGTH];
    int power;
    char type[MAX_NAME_LENGTH];
} Move;

// Struct for representing a Pokemon
typedef struct {
    char name[MAX_NAME_LENGTH]; 
    char type[MAX_NAME_LENGTH];
    int hp;
    Move moves[MAX_MOVES];
} Pokemon;

// Struct for representing a Pokemon team
typedef struct {
    Pokemon team[6];
} PokemonTeam;

int main(){
    Move thunder = {"Thunder", 90, "Electric"};
    Move earthquake = {"Earthquake", 100, "Ground"};
    Move tackle = {"Tackle", 20, "Normal"};
    Move flamethrower = {"Flamethrower", 90, "Fire"};
    Move fly = {"Fly", 90, "Flying"};
    Move dragonClaw = {"Dragon Claw", 50, "Dragon"};
    Move quickAttack = {"Quick Attack", 30, "Fly"};
    Move ironTail = {"Iron Tail", 60, "Steel"};
    Move fireBlast = {"FireBlast", 70, "Fire"};
    Move splash = {"Splash", 0 , "Normal"};
    Move tailWhip = {"Tail Whip", 0, "Normal"};
    Move growl = {"Growl", 0, "Normal"};


    Pokemon pikachu = {"Pikachu", "Electric", 100, {thunder, earthquake, quickAttack, ironTail}};
    Pokemon charizard = {"Charizard", "Fire", 120, {flamethrower, fly, dragonClaw, fireBlast}};
    Pokemon rattata  = {"Rattata", "Normal", 50, {quickAttack, tackle, tailWhip, splash}};
    Pokemon dratini = {"Dratini","Dragon", 70, {splash, quickAttack, dragonClaw, ironTail}};
    Pokemon pidgey = {"Pidgey","Flying", 50, {quickAttack, fly, tailWhip, growl}};

    int userInput;
    PokemonTeam myTeam = {pikachu, charizard};
    Pokemon wildPokemon[2] = {rattata, pidgey};
    srand(time(NULL));

    while(userInput != 0){
        printf("Main menu please pick an option:\n");
        printf("1. Search for a pokemon\n");
        printf("2. Lower your first pokemons hp by 20 for demo purpose::::\n");
        printf("3. Display your first pokemons health.\n");
        printf("0 Exit the program:\n");
        scanf("%d", &userInput);
        
    switch (userInput) {
        case 1:
            // Code to be executed if expression matches constant1
            printf("Searching..........\n");
            int random_number = rand() % 6;
            if (random_number == 2 || random_number == 4){
                printf("You have found a Pokemon.\n");
                int random_index = rand() % 3; // Randomly choose a Pokemon from the array
                Pokemon encounter = wildPokemon[random_index];
                int j = 1;
                while(j != 0){
                    int userSelection = 0;
                    printf("Wild pokemon you encountered is: %s\n", encounter.name);
                    printf("Type: %s\n", encounter.type);
                    printf("Current hp:  %d\n", encounter.hp);
                    printf("Choose what you would like to do:\n");
                    printf("1. Fight\n");
                    printf("2. Run\n");
                    scanf("%d", &userSelection);
                    if (userSelection == 1){
                        //todo add fight logic
                    }else if(userSelection == 2){
                        printf("You ran from the battle.....\n");
                        j = 0;
                    }else{
                        printf("You did not choose a valid option please try again.\n");
                    }
                }
            }else{
                printf("You have not found a pokemon better luck next time.....\n");
            }
            break;
        case 2:
            // Code to be executed if expression matches constant2
            myTeam.team[0].hp -= 20;
            break;
        // More cases can be added as needed
        case 3:
            printf("Pikachu's current hp is: %d\n", myTeam.team[0].hp);
            break;
        case 0:
            printf("ThankYou for Playing......");
            break;
        default:
            // Code to be executed if expression doesn't match any constant
            printf("Number did not match any none options.");
        }
    }