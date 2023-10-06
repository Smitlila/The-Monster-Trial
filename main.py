'''
MONSTER TRIAL GAME
A a game where the user must defeat three monsters to pass the trials. Use the following
UML diagram and the method descriptions below to create your program.

Smit Lila: main.py / entity.py / hero.py / enemy_factory.py / goblin.py / easygoblin.py / ogre.py / beg_factory.py / exp_factory.py / troll.py / easytroll.py / easyogre.py 
'''
# Import necessary modules and classes
from entity import Entity
from hero import Hero
from enemy_factory import EnemyFactory
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory
from goblin import Goblin
from ogre import Ogre
from troll import Troll
from easy_goblin import EasyGoblin
from easy_ogre import EasyOgre
from easy_troll import EasyTroll
import random

# Define the main function
def main():
    # Print welcome message
    print("Monster Trials\n")

    # Get player's name and introduce the game
    player_name = input("What is your name? ")
    print(f"You will face a series of 3 monsters, {player_name}.")
    print("Defeat them all to win.\n")

    # Create the hero instance
    hero = Hero(player_name)

    # Ask the player to select the difficulty level
    print("Select Difficulty:")
    print("1.Beginner \n2.Expert")
    difficulty = int(input('Enter choice: '))

    # Validate the player's input
    while difficulty not in (1,2):
        print("Invalid Input")
        difficulty = int(input('Enter choice: '))

    # Create the enemy factory instance based on the difficulty level
    if difficulty == 1:
        factory = BeginnerFactory()
    elif difficulty == 2:
        factory = ExpertFactory()

    # Create three random monsters
    monsters = [factory.create_random_enemy() for _ in range(3)]

    # Start the battle loop
    while hero.hp() > 0 and len(monsters) > 0:

        # Show the available monsters
        print("\nChoose an enemy to attack:")
        for i, monster in enumerate(monsters):
            print("{}: {}".format(i + 1, monster))

        # Get the player's choice of monster to attack
        enemy = int(input('Enter choice: '))
        while enemy not in range(1,len(monsters)+1):
            print("Invalid Input")
            enemy = int(input('Enter choice: '))
        
        monster = monsters[enemy-1]

        # Show the hero's HP and attack options
        print(f"\n{player_name} HP: {hero.hp()}")
        print("1. Sword Attack \n2. Arrow Attack")
        attack_type = int(input("Enter choice: "))

        # Validate the player's input
        while attack_type not in (1,2):
            print("Invalid Input")
            attack_type = int(input("Enter choice: "))

        # Perform the selected attack and show the result
        if attack_type == 1:
            des = hero.melee_attack(monster)
        elif attack_type == 2:
            des = hero.ranged_attack(monster)

        print(f'\n{des}')
        
        # Check if the monster is defeated or not
        if monster.hp() <= 0:
            print(f"\nYou have Slain the {monster.name()}")
            monsters.remove(monster)
        else:
            # If the monster is not defeated, perform its attack and show the result
            des = monster.melee_attack(hero)
            print(f'\n{des}')

        # Check if the game is over
        if len(monsters) == 0:
            print("\nCongratulations! You defeated all three monsters! \nGame Over!!!!")

        if hero.hp() == 0:
            print(f'\n{player_name} killed by {monster.name()}\nYou Loose!!')
            
# Call the main function to start the game
main()
