class Entity():
    # Define a constructor that initializes the name and hp attributes
    def __init__(self, name, hp):
        self._name = name  
        self._hp = hp

    # Define a method called hp that returns the current hp of the entity
    def hp(self):
        return self._hp

    # Define a method called name that returns the name of the entity
    def name(self):
        return self._name

    # Define a method called take_damage that subtracts the damage from the hp of the entity
    def take_damage(self, dmg):
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0

    # Define a method called __str__ that returns a string representation of the entity's name and hp
    def __str__(self):
        return f"{self._name}: {self._hp}"

    # Define a method called melee_attack that takes another entity as a parameter and does nothing
    def melee_attack(self, entity):
        pass
