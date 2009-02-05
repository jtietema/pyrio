
import pygame
import os

from game_entity import GameEntity

class Tile(GameEntity):
    def __init__(self, name, (x, y)):
        self.image = pygame.image.load(os.path.join('..', 'assets', 'images', 'ground', name + '.png')).convert()
        
        GameEntity.__init__(self, (x, y), self.image.get_size())
    
    def render(self, screen, screen_position):
        screen.blit(self.image, screen_position)