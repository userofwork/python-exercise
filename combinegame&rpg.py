import time
import random

# Define a function to print a colored message
def print_color(text, color):
    print(f"\033[{color}m{text}\033[0m")

# Print a colored welcoming message
print_color("**********************************************", "38")
print_color("*                                            *", "32")
print_color("*                                            *", "32")
print_color("*              WELCOME TO PUBG RPG           *", "33")
print_color("*                                            *", "32")
print_color("*                                            *", "32")
print_color("**********************************************", "39")
print_color("\nSurvive the battle and become the last player standing!\n", "36")
time.sleep(1)  # Wait for 1 second before proceeding to the game

class Player:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

class Monster:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

def battle(player, monster):
    print(f"A {monster.name} appears!")
    while player.health > 0 and monster.health > 0:
        player_attack = random.randint(1, player.strength)
        monster_attack = random.randint(1, monster.strength)
        player_defense = random.randint(1, player.defense)
        monster_defense = random.randint(1, monster.defense)

        player_damage = max(0, player_attack - monster_defense)
        monster_damage = max(0, monster_attack - player_defense)

        player.health -= monster_damage
        monster.health -= player_damage

        print(f"{player.name} attacks {monster.name} for {player_damage} damage!")
        print(f"{monster.name} attacks {player.name} for {monster_damage} damage!")
        print(f"{player.name} has {player.health} health remaining!")
        print(f"{monster.name} has {monster.health} health remaining!")

    if player.health > 0:
        print(f"{player.name} defeats {monster.name}!")
    else:
        print(f"{player.name} has been defeated by {monster.name}.")

# Create the player and monster
player = Player("Hero", 100, 10, 5)
monster = Monster("Goblin", 50, 5, 2)

# Start the battle
battle(player, monster)
