from enemy_factory import EnemyFactory
import random
from easy_goblin import EasyGoblin
from easy_ogre import EasyOgre
from easy_troll import EasyTroll


class BeginnerFactory(EnemyFactory):
    # Define a method to create random enemies from a list of enemy types
    def create_random_enemy(self):
        
        # Create a list of enemy types
        enemy_types = [EasyGoblin(), EasyOgre(), EasyTroll()]
        
        # Return a randomly chosen enemy type from the list
        return random.choice(enemy_types)
