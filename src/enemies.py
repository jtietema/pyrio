from animation import Animation
from enemy import Enemy
from game_entity import GameEntity

from states.enemies.krush.walking import WalkingState as KrushWalkingState
from states.enemies.krush.flat import FlatState as KrushFlatState
from states.enemies.turtle.walking import WalkingState as TurtleWalkingState

class Krush(Enemy):
    def __init__(self, position, map):
        Enemy.__init__(self, position, (64, 50), map)
        
        self.states = {
            'walk': KrushWalkingState(self),
            'flat': KrushFlatState(self)
        }
        self.currentState = self.states['walk']

class Turtle(Enemy):
    def __init__(self, position, map):
        Enemy.__init__(self, position, (64, 64), map)
        
        self.states = {
            'walk': TurtleWalkingState(self)
        }
        self.currentState = self.states['walk']