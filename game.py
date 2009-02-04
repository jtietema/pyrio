
from world import World

class Game():
    def __init__(self):
        self.world = World()
        
    def update(self, state):
        self.world.update(state)
        
    def render(self, screen):
        self.world.render(screen)