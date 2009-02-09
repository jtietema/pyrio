
from pygame.locals import *
import os

from moveable_entity import MoveableEntity
from game_entity import GameEntity
from animation import Animation

class Player(MoveableEntity):
    def __init__(self, map):
        MoveableEntity.__init__(self, (0, 0), (64, 64), map)
        
        self.x_speed = .2
        self.y_speed = .2
        
        self.animations = {
            'stand_left': Animation('player', ('stand_left',), GameEntity.FRAME_LENGTH),
            'stand_right': Animation('player', ('stand_right',), GameEntity.FRAME_LENGTH),
            'walk_left': Animation('player', ('walk_left_1', 'walk_left_2'), GameEntity.FRAME_LENGTH),
            'walk_right': Animation('player', ('walk_right_1', 'walk_right_2'), GameEntity.FRAME_LENGTH)
        }
        
        self.animation = self.animations['stand_right']
        self.direction = GameEntity.DIRECTION_RIGHT
        
    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        x_delta = time_passed * self.x_speed
        y_delta = time_passed * self.y_speed
        
        pressed_keys = tick_data['pressed_keys']
        if pressed_keys[K_LEFT]:
            x_delta *= -1
            animation_name = 'walk_left'
            self.direction = GameEntity.DIRECTION_LEFT
        elif pressed_keys[K_RIGHT]:
            animation_name = 'walk_right'
            self.direction = GameEntity.DIRECTION_RIGHT
        else:
            x_delta = 0
            if self.direction is GameEntity.DIRECTION_LEFT:
                animation_name = 'stand_left'
            else:
                animation_name = 'stand_right'
        
        self.animation = self.animations[animation_name]
        
        if pressed_keys[K_UP]:
            y_delta *= -1
        elif pressed_keys[K_DOWN]:
            y_delta *= 1
        else:
            y_delta = 0
        
        x_delta, y_delta = self.map.collisions((self.x, self.y), (x_delta, y_delta))
        self.x += x_delta
        self.y += y_delta
        
    def render(self, screen):        
        x_screen = screen.get_width() / 2 - self.width / 2
        y_screen = screen.get_height() / 2 - self.height / 2
        screen.blit(self.animation.get_image(), (x_screen, y_screen))
        
