
from pygame.locals import *

from movable_entity import MovableEntity
from game_entity import GameEntity
from animation import Animation

class Player(MovableEntity):
    MAX_JUMPING_TIME = 600
    
    def __init__(self, position, map):
        MovableEntity.__init__(self, position, (56, 64), map)
        
        self.x_speed = .2
        self.y_speed = .2

        self.jumping = False
        self.jumping_time = 0
        
        self.animations = {
            'stand_left': Animation('player', ('stand_left',), GameEntity.FRAME_LENGTH),
            'stand_right': Animation('player', ('stand_right',), GameEntity.FRAME_LENGTH),
            'walk_left': Animation('player', ('walk_left_1', 'walk_left_2'), GameEntity.FRAME_LENGTH),
            'walk_right': Animation('player', ('walk_right_1', 'walk_right_2'), GameEntity.FRAME_LENGTH),
            'fall_left' : Animation('player', ('fall_left', ), GameEntity.FRAME_LENGTH),
            'fall_right': Animation('player', ('fall_right',), GameEntity.FRAME_LENGTH),
            'jump_left' : Animation('player', ('jump_left', ), GameEntity.FRAME_LENGTH),
            'jump_right': Animation('player', ('jump_right',), GameEntity.FRAME_LENGTH)
        }
        
        self.animation = self.animations['stand_right']
        self.direction = GameEntity.DIRECTION_RIGHT
        
    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        x_delta = time_passed * self.x_speed
        y_delta = time_passed * self.y_speed
        
        pressed_keys = tick_data['pressed_keys']
        animation_name = 'walk'
        if pressed_keys[K_LEFT]:
            x_delta *= -1
            self.direction = GameEntity.DIRECTION_LEFT
        elif pressed_keys[K_RIGHT]:
            self.direction = GameEntity.DIRECTION_RIGHT
        else:
            x_delta = 0
            animation_name = 'stand'
        
        if pressed_keys[K_UP] and ((not self.falling and not self.jumping) or
                self.jumping) and not self.jumping_time > Player.MAX_JUMPING_TIME:
            self.jumping = True
        else:
            self.jumping = False
            self.jumping_time = 0
            y_delta = 0

        if self.jumping:
            y_delta = time_passed * self.y_speed * -2
            self.jumping_time += time_passed
            animation_name = 'jump'
            if self.jumping_time > Player.MAX_JUMPING_TIME:
                self.jumping = False
                self.jumping_time = 0

        self.falling = self.check_falling(time_passed * self.y_speed * 2)
        if not self.jumping and self.falling:
            y_delta = time_passed * self.y_speed * 2
            animation_name = 'fall'

        # Execute the move if there are no collisions
        if (x_delta is not 0 or y_delta is not 0 ):
            if not self.map.collisions(self, (x_delta, y_delta)):
                self.rect = self.rect.move(x_delta, y_delta)
            elif not self.map.collisions(self, (0, y_delta)):
                self.rect = self.rect.move(0, y_delta)

        if self.direction is GameEntity.DIRECTION_LEFT:
            animation = '%s_%s' % (animation_name, 'left')
        else:
            animation = '%s_%s' % (animation_name, 'right')
        self.animation = self.animations[animation]
        
    def render(self, screen):        
        x_screen = screen.get_width() / 2 - self.rect.width / 2
        y_screen = screen.get_height() / 2 - self.rect.height / 2
        screen.blit(self.animation.get_image(), (x_screen, y_screen))
        
