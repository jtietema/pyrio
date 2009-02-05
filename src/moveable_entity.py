
from game_entity import GameEntity

class MoveableEntity(GameEntity):
    def __init__(self, (x,y), (width, height), map):
        GameEntity.__init__(self, (x,y), (width, height))

        self.map = map
        
