from animation import Animation
from enemy import Enemy
from game_entity import GameEntity

class Krush(Enemy):
    def __init__(self, position, map):
        Enemy.__init__(self, position, map)
        
        self.x_speed = .25
        
        self.animations = {
            'walk_left': Animation(('enemies', 'krush'), ('walk_left_1', 'walk_left_2', 'walk_left_3'), 100),
            'walk_right': Animation(('enemies', 'krush'), ('walk_right_1', 'walk_right_2', 'walk_right_3'), 100)
        }
        
        self.direction = GameEntity.DIRECTION_RIGHT
        self.animation = self.animations['walk_right']
        
class Turtle(Enemy):
    def __init__(self, position, map):
        Enemy.__init__(self, position, map)
        
        self.x_speed = .1
        
        self.animations = {
            'walk_left': Animation(('enemies', 'turtle'), ('walk_left_1', 'walk_left_2', 'walk_left_3'), 150),
            'walk_right': Animation(('enemies', 'turtle'), ('walk_right_1', 'walk_right_2', 'walk_right_3'), 150)
        }
        
        self.direction = GameEntity.DIRECTION_RIGHT
        self.animation = self.animations['walk_right']