import time
import random

# Define a function to print a colored message
def print_color(text, color):
    print(f"\033[{color}m{text}\033[0m")

# Print a colored welcoming message
print_color("**********************************************", "95")
print_color("*                                            *", "94")
print_color("*               WELCOME TO PUBG RPG          *", "93")
print_color("*                                            *", "92")
print_color("**********************************************", "91")
print_color("\nSurvive the battle and become the last player standing!\n", "96")
time.sleep(1)  # Pause for dramatic effect

# Define player and enemy classes
class Player:
    def __init__(self, name, health, damage, defense):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

class Enemy:
    def __init__(self, name, health, damage, defense):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense

def battle(player, enemy):
    print(f"\nA wild {enemy.name} appears!")

    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name} has {player.health} health left.")
        print(f"{enemy.name} has {enemy.health} health left.")

        player_choice = input("\nDo you want to attack (a) or heal (h)? ")
        if player_choice == "a":
            enemy.health -= player.damage
            print(f"You attack {enemy.name} for {player.damage} damage!")
        elif player_choice == "h":
            player.health += 20  # Example healing value
            print(f"You heal yourself for 20 health!")
        else:
            print("Invalid input. Try again.")
            continue

        # Check for enemy defeat
        if enemy.health <= 0:
            print(f"\n{enemy.name} has been defeated!")
            return

        # Enemy's turn
        enemy_attack = random.randint(1, enemy.damage)
        player.health -= enemy_attack
        print(f"{enemy.name} attacks you for {enemy_attack} damage!")

        # Check for player defeat
        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            return

# Create the player and an enemy
player = Player("Hero", 100, 20, 5)  # Example player
enemy = Enemy("Goblin", 50, 10, 2)  # Example enemy

# Start the game
battle(player, enemy)
