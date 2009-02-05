
import pygame
import os

from game_entity import GameEntity

class Tile(GameEntity):
    def __init__(self, name, (x, y)):
        GameEntity.__init__(self, (x, y), (64, 64))
        
        self.image = pygame.image.load(os.path.join('assets', 'ground', name + '.png')).convert()
    
    def render(self, screen, position):
        screen.blit(self.image, position)