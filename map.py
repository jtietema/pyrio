
import pygame
from pygame.locals import *
import os

class Map():    
    def __init__(self, player):
        self.player = player
        self.speed = .3
        self.x_offset = 0
        
        self.tiles = (
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png',
            'up.png'
        )
        
        self.tile_images = {
            'up.png': pygame.image.load(os.path.join('assets', 'ground', 'up.png')).convert()
        }
        
    def update(self, tick_data):
        x_delta = tick_data['time_passed'] * self.speed
        
        if tick_data['pressed_keys'][K_LEFT]:
            self.x_offset += x_delta
        if tick_data['pressed_keys'][K_RIGHT]:
            self.x_offset -= x_delta
        
    def render(self, screen):
        y = screen.get_height() - 64
        
        screen_width = screen.get_width()
        
        tile_width = 64
        total_width = len(self.tiles) * tile_width
        
        x = self.x_offset
        
        for (index, tile_filename) in enumerate(self.tiles):
            if x + tile_width > 0 or x < screen_width:
                tile_image = self.tile_images[tile_filename]
                screen.blit(tile_image, (x, y))
            x += tile_width
        