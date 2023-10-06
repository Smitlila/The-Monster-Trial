import random
from entity import Entity

class Goblin(Entity):
    # Define a constructor that calls the constructor of Entity and sets the Goblin's name and health points
    def __init__(self):
        super().__init__("Goblin", random.randint(10, 14))

    # Define a method called melee_attack that takes another entity as a parameter and deals random damage to it
    def melee_attack(self, entity):
        # Generate a random damage value
        dmg = random.randint(8, 12)
        # Apply the damage to the other entity
        entity.take_damage(dmg)
        # Return a string describing the attack
        return f"{self.name()} bites {entity.name()} for {dmg} damage!"

