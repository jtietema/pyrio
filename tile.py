
import pygame
import os

from game_entity import GameEntity
from asset_manager import AssetManager

class Tile(GameEntity):
    def __init__(self, name, (x, y)):
        self.image = AssetManager.get_image('ground', name + '.png')
        
        GameEntity.__init__(self, (x, y), self.image.get_size())
    
    def render(self, screen, screen_position):
        screen.blit(self.image, screen_position)