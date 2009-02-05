
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
        
        # self.width = sum([tile.get_width() for tile in self.tiles])
        # self.height = 600
        
    def update(self, tick_data):
        screen_width, screen_height = tick_data['screen_size']
        x, y = self.player.get_position()
        
        self.x_offset = x - (screen_width / 2)
        self.y_offset = y - (screen_height / 2)
        
    def render(self, screen):
        screen_width, screen_height = screen.get_size()
        
        for tile in self.tiles:
            if tile != None:
                tile_width, tile_height = tile.get_size()
                
                tile_screen_y = tile.get_y() - self.y_offset
                tile_screen_x = tile.get_x() - self.x_offset
        
                if ((tile_screen_x + tile_width > 0 or tile_screen_x < screen_width) and (tile_screen_y + tile_height > 0 or tile_y < screen_height)):
                    tile.render(screen, (tile_screen_x, tile_screen_y))
        