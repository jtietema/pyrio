
import pygame
from pygame.locals import *
import os

class Map():    
    def __init__(self, player):
        self.player = player
        self.speed = .2
        self.x_offset = 0
        
        self.tile_dimensions = (64, 64)
        
        self.tiles = ('up.png', ) * 30
        
        self.width = len(self.tiles) * self.tile_dimensions[0]
        
        # USE ASSET MANAGER HERE
        self.tile_images = {
            'up.png': pygame.image.load(os.path.join('assets', 'ground', 'up.png')).convert()
        }
        
    def update(self, tick_data):
        x_delta = tick_data['time_passed'] * self.speed
        
        if tick_data['pressed_keys'][K_LEFT]:
            self.x_offset += x_delta
        if tick_data['pressed_keys'][K_RIGHT]:
            self.x_offset -= x_delta
        
        # Determine clipping
        self.x_offset = min(0, self.x_offset)
        # SCREEN SIZE NOT AVAILABLE HERE
        self.x_offset = max(self.x_offset, -(self.width - 800))
        
    def render(self, screen):        
        screen_width, screen_height = screen.get_size()
        tile_width, tile_height = self.tile_dimensions
        
        y = screen_height - tile_height
        x = self.x_offset
        
        for (index, tile_filename) in enumerate(self.tiles):
            if x + tile_width > 0 or x < screen_width:
                tile_image = self.tile_images[tile_filename]
                screen.blit(tile_image, (x, y))
            
            x += tile_width
        