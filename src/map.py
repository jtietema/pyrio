
import pygame
from pygame.locals import *
import os

from tile import Tile

class Map():
    def __init__(self):
        self.player = None
        
        self.x_offset = 0
        self.y_offset = 0
        
        self.tiles = (
            Tile('up', (0, 200)),
            Tile('up', (64, 200)),
            Tile('up', (128, 200)),
            Tile('up', (192, 200)),
            Tile('up', (256, 200)),
            Tile('up', (320, 200))
        )
        
        self.width = sum([tile.get_width() for tile in self.tiles])
        self.height = 600
        
    def update(self, tick_data):
        screen_width, screen_height = tick_data['screen_size']
        x, y = self.player.get_position()
        
        self.x_offset = x - (screen_width / 2)
        self.y_offset = y - (screen_height / 2)
        
    def render(self, screen):
        screen_width, screen_height = screen.get_size()
        
        for tile in self.tiles:
            tile_width, tile_height = tile.get_size()
            tile_screen_x = tile.get_x() - self.x_offset
            tile_screen_y = tile.get_y() - self.y_offset
            
            if ((tile_screen_x + tile_width > 0 or tile_screen_x < screen_width) and (tile_screen_y + tile_height > 0 or tile_y < screen_height)):
                tile.render(screen, (tile_screen_x, tile_screen_y))
    def collisions(self, (x,y), (delta_x, delta_y)):
        min_x = delta_x
        min_y = delta_y
        for tile in self.tiles:
            tile_x, tile_y = tile.collision((x,y), (delta_x, delta_y))
            if tile_x < min_x:
                min_x = tile_x
            if tile_y < min_y:
                min_y = tile_y
        return (min_x, min_y)
        
    def add_player(self, player):
        self.player = player
        
