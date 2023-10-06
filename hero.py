# Importing the random module to generate random integers
import random
# Importing the Entity class from the entity module
from entity import Entity

# Defining the Hero class as a subclass of Entity
class Hero(Entity):
    # Initializing the class with a name and default health points
    def __init__(self, name):
        self._name = name  # Assigning the name parameter to the _name attribute
        self._hp = 25      # Setting the default health points to 25

    # Getter method for the _hp attribute
    def hp(self):
        return self._hp

    # Method for performing a melee attack on another entity
    def melee_attack(self, entity):
        # Generating two random integers from 1 to 6, and summing them
        dmg = sum(random.randint(1, 6) for _ in range(2))
        # Calling the take_damage method of the target entity with the damage value
        entity.take_damage(dmg)
        # Returning a string describing the attack and its damage value
        return f"{self.name()} slashes a {entity.name()} with a sword for {dmg} damage."

    # Method for performing a ranged attack on another entity
    def ranged_attack(self, entity):
        # Generating a random integer from 1 to 12
        dmg = random.randint(1, 12)
        # Calling the take_damage method of the target entity with the damage value
        entity.take_damage(dmg)
        # Returning a string describing the attack and its damage value
        return f"{self.name()} pierces a {entity.name()} with an arrow for {dmg} damage."
