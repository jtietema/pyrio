
import pygame
from pygame.locals import *
import os
from game_entity import GameEntity

class Player(GameEntity):
    def __init__(self):
        # TODO call GameEntity init
        
        # the image data
        # standing
        self.stand = self.load_twodirectional_asset(os.path.join('assets', 'player', 'stand_right.png'), (64,64))
        
        # walking
        self.walk_1 = self.load_twodirectional_asset(os.path.join('assets', 'player', 'walk_right_1.png'), (64,64))
        self.walk_2 = self.load_twodirectional_asset(os.path.join('assets', 'player', 'walk_right_2.png'), (64,64))
        
        # the state properties
        self.right = True
        self.walking = False
        self.walkingCounter = 0
        
    def update(self, tick_data):
        pressed_keys = tick_data['pressed_keys']
        if pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]:
            if pressed_keys[K_LEFT]:
                self.right = False
            else:
                self.right = True
            self.walking = True
            self.walkingCounter += tick_data['time_passed']
            if self.walkingCounter > 600:
                self.walkingCounter = 0
        else:
            self.walking = False
            self.walkingCounter = 0
        
    def render(self, screen):
        if self.right:
            direction = 1
        else:
            direction = 0
        if self.walking:
            if self.walkingCounter > 300:
                screen.blit(self.walk_2[direction], (400-32, 400-64))
            else:
                screen.blit(self.walk_1[direction], (400-32, 400-64))
        else:
            screen.blit(self.stand[direction], (400-32, 400-64))
        