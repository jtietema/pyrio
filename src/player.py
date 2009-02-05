
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
        self.right = True
        self.walking = False
        self.walking_counter = 0
        
    def update(self, tick_data):
        time_passed = tick_data['time_passed']
        x_delta = time_passed * self.x_speed
        y_delta = time_passed * self.y_speed
        
        pressed_keys = tick_data['pressed_keys']
        if pressed_keys[K_LEFT]:
            #self.x -= x_delta
            x_delta *= -1
        elif pressed_keys[K_RIGHT]:
            #self.x += x_delta
            x_delta *= 1
        else:
            x_delta = 0
        if pressed_keys[K_UP]:
            #self.y -= y_delta
            y_delta *= -1
        elif pressed_keys[K_DOWN]:
            #self.y += y_delta
            y_delta *= 1
        else:
            y_delta = 0
        
        x_delta, y_delta = self.map.collisions((self.x, self.y), (x_delta, y_delta))
        self.x += x_delta
        self.y += y_delta
        
        if pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]:
            if pressed_keys[K_LEFT]:
                self.right = False
            else:
                self.right = True
            self.walking = True
            self.walking_counter += tick_data['time_passed']
            if self.walking_counter > 600:
                self.walking_counter = 0
        else:
            self.walking = False
            self.walking_counter = 0
        
    def render(self, screen):
        if self.right:
            direction = 1
        else:
            direction = 0
        if self.walking:
            if self.walking_counter > 300:
                screen.blit(self.walk_2[direction], (400-32, 400-64))
            else:
                screen.blit(self.walk_1[direction], (400-32, 400-64))
        else:
            screen.blit(self.stand[direction], (400-32, 400-64))
        
