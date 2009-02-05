
import pygame
from pygame.locals import *
import os

class Map():
    def __init__(self, player):
        self.player = player
        
        self.x_offset = 0
        self.y_offset = 0
        
        self.tile_dimensions = (64, 64)
        self.tiles = ('up.png', ) * 30
        
        self.width = len(self.tiles) * self.tile_dimensions[0]
        self.height = 600
        
        # USE ASSET MANAGER HERE
        self.tile_images = {
            'up.png': pygame.image.load(os.path.join('assets', 'ground', 'up.png')).convert()
        }
        
    def update(self, tick_data):
        screen_width, screen_height = tick_data['screen_size']
        x, y = self.player.get_position()
        
        self.x_offset = x - (screen_width / 2)
        self.y_offset = y - (screen_height / 2)
        
    def render(self, screen):
        screen_width, screen_height = screen.get_size()
        tile_width, tile_height = self.tile_dimensions
        
        cur_tile_x = 0
        cur_tile_y = self.height - tile_height
        
        # Constant y
        tile_y = cur_tile_y - self.y_offset
        
        for (index, tile_filename) in enumerate(self.tiles):
            tile_x = cur_tile_x - self.x_offset
            
            # if (self.x_offset + tile_width > 0 or x < screen_width):
            tile_image = self.tile_images[tile_filename]
            screen.blit(tile_image, (tile_x, tile_y))
            
            cur_tile_x += tile_width
        