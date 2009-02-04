
import pygame
import os

class Map():
    def __init__(self, player):
        self.player = player
        self.groundUp = pygame.image.load(os.path.join('assets', 'ground', 'up.png')).convert()
        
    def update(self, tick_data):
        pass
        
    def render(self, screen):
        for i in range(13):
            screen.blit(self.groundUp, (i*64, 400))
        