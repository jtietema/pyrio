
import pygame
import os

class Player():
    def __init__(self):
        self.stand_right = pygame.image.load(os.path.join('assets', 'player', 'stand_right.png')).convert_alpha()
        self.stand_right = pygame.transform.smoothscale(self.stand_right, (64,64))
        self.stand_left = pygame.transform.flip(self.stand_right, True, False)
        
    def update(self, tick_data):
        pass
        
    def render(self, screen):
        screen.blit(self.stand_right, (400-32, 400-64))