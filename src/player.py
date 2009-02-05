
from pygame.locals import *
import os

from moveable_entity import MoveableEntity

class Player(MoveableEntity):
    def __init__(self, map):
        MoveableEntity.__init__(self, (0, 0), (64, 64), map)
        
        self.x_speed = .2
        self.y_speed = .2
        
        # the image data
        # standing
        self.stand = self.load_twodirectional_asset(os.path.join('..', 'assets', 'images', 'player', 'stand_right.png'), (64,64))
        
        # walking
        self.walk_1 = self.load_twodirectional_asset(os.path.join('..', 'assets', 'images', 'player', 'walk_right_1.png'), (64,64))
        self.walk_2 = self.load_twodirectional_asset(os.path.join('..', 'assets', 'images', 'player', 'walk_right_2.png'), (64,64))
        
        # the state properties
        self.direction = GameEntity.DIRECTION_RIGHT
        self.walking_counter = 0
        
    def update(self, tick_data):
        time_passed = tick_data['time_passed']
        x_delta = time_passed * self.x_speed
        y_delta = time_passed * self.y_speed
        
        self.walking = False
        
        pressed_keys = tick_data['pressed_keys']
        if pressed_keys[K_LEFT]:
            x_delta *= -1
            self.direction = GameEntity.DIRECTION_LEFT
            self.walking = True
        elif pressed_keys[K_RIGHT]:
            self.direction = GameEntity.DIRECTION_RIGHT
            self.walking = True
        else:
            x_delta = 0
        
        if pressed_keys[K_UP]:
            y_delta *= -1
        elif pressed_keys[K_DOWN]:
            y_delta *= 1
        else:
            y_delta = 0
        
        x_delta, y_delta = self.map.collisions((self.x, self.y), (x_delta, y_delta))
        self.x += x_delta
        self.y += y_delta
        
        if self.walking:
            self.walking_counter += time_passed
            if self.walking_counter > 600:
                self.walking_counter = 0
        else:
            self.walking_counter = 0
        
    def render(self, screen):        
        if self.walking:
            if self.walking_counter > 300:
                image = self.walk_2[self.direction]
            else:
                image = self.walk_1[self.direction]
        else:
            image = self.stand[self.direction]
        
        x_screen = screen.get_width() / 2 - self.width / 2
        y_screen = screen.get_height() / 2 - self.height / 2
        screen.blit(image, (x_screen, y_screen))
        
