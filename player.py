
import pygame
from pygame.locals import *
import os

class Player():
    def __init__(self):
        # the image data
        # standing
        self.stand = self.load_assets(os.path.join('assets', 'player', 'stand_right.png'))
        
        # walking
        self.walk_1 = self.load_assets(os.path.join('assets', 'player', 'walk_right_1.png'))
        self.walk_2 = self.load_assets(os.path.join('assets', 'player', 'walk_right_2.png'))
        
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
            if self.walkingCounter > 900:
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
            if self.walkingCounter > 600:
                screen.blit(self.walk_2[direction], (400-32, 400-64))
            else:
                screen.blit(self.walk_1[direction], (400-32, 400-64))
        else:
            screen.blit(self.stand[direction], (400-32, 400-64))
        
    def load_assets(self, path):
        right = pygame.image.load(path).convert_alpha()
        right = pygame.transform.smoothscale(right, (64,64))
        left = pygame.transform.flip(right, True, False)
        return (left, right)