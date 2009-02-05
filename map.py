
import pygame
from pygame.locals import *
import os

from tile import Tile
from map_serializer import MapSerializer

class Map():
    def __init__(self, name, player):
        self.tiles = MapSerializer.deserialize(name)
        
        self.player = player
        
        self.x_offset = 0
        self.y_offset = 0
        
        self.width = max([tile.get_x() + tile.get_width() for tile in self.tiles])
        self.height = max([tile.get_y() + tile.get_height() for tile in self.tiles])
        
    def update(self, tick_data):
        screen_width, screen_height = tick_data['screen_size']
        x, y = self.player.get_real_position()
        
        self.x_offset = x - (screen_width / 2)
        self.y_offset = y - (screen_height / 2)
        
    def render(self, screen):
        screen_width, screen_height = screen.get_size()
        
        for tile in self.tiles:
            if tile != None:
                tile_width, tile_height = tile.get_size()
                
                tile_y_screen = tile.get_y() - self.y_offset
                tile_x_screen = tile.get_x() - self.x_offset
        
                if ((tile_x_screen + tile_width > 0 or tile_x_screen < screen_width) and (tile_y_screen + tile_height > 0 or tile_y_screen < screen_height)):
                    tile.render(screen, (tile_x_screen, tile_y_screen))
        