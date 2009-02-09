
from game_entity import GameEntity
from movable_entity import MovableEntity
from animation import Animation

class Enemy(MovableEntity):
    def __init__(self, position, map):
        MovableEntity.__init__(self, position, (64, 64), map)
    
        self.x_speed = .2
        
        self.animations = {
            'walk_left': Animation('enemy', ('walk_left_1', 'walk_left_2', 'walk_left_3'), GameEntity.FRAME_LENGTH),
            'walk_right': Animation('enemy', ('walk_right_1', 'walk_right_2', 'walk_right_3'), GameEntity.FRAME_LENGTH)
        }
        
        self.direction = GameEntity.DIRECTION_RIGHT
        self.animation = self.animations['walk_right']
    
    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        x_delta = time_passed * self.x_speed
        
        if self.direction is GameEntity.DIRECTION_LEFT:
            x_delta *= -1
        
        y_delta = 0
        
        if x_delta is not 0 or y_delta is not 0:
            if self.map.collisions(self, (x_delta, y_delta)):
                # Flip the direction because of collisions
                if self.direction is GameEntity.DIRECTION_LEFT:
                    self.direction = GameEntity.DIRECTION_RIGHT
                else:
                    self.direction = GameEntity.DIRECTION_LEFT
            else:
                # Otherwise, move the enemy to the desired location
                self.rect = self.rect.move(x_delta, y_delta)
        
        self.animation = self.animations['walk_%s' % self.direction]
    
    def render(self, screen, offsets):
        GameEntity.render(self, screen, self.animation.get_image(), offsets)
