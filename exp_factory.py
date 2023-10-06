from enemy_factory import EnemyFactory
import random
from goblin import Goblin
from ogre import Ogre
from troll import Troll

class ExpertFactory(EnemyFactory):
    # Define a method to create random enemies from a list of enemy types
    def create_random_enemy(self):
        
        # Create a list of enemy types
        enemy_types = [Goblin(), Ogre(), Troll()]
        
        # Return a randomly chosen enemy type from the list
        return random.choice(enemy_types)
