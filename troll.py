import random
from entity import Entity

class Troll(Entity):
    # Define a constructor that calls the constructor of Entity and sets the Troll's name and health points
    def __init__(self):
        super().__init__("Troll", random.randint(6, 10))

    # Define a method called melee_attack that takes another entity as a parameter and deals random damage to it
    def melee_attack(self, entity):
        # Generate a random damage value
        dmg = random.randint(5, 8)
        # Apply the damage to the other entity
        entity.take_damage(dmg)
        # Return a string describing the attack
        return f"{self.name()} slashes {entity.name()} for {dmg} damage!"
