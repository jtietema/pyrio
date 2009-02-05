
import pygame

class GameEntity():
    def __init__(self, (x,y), (width, height)):
        # position
        self.x = x
        self.y = y
        
        # size
        self.width = width
        self.height = height
    
    def load_twodirectional_asset(self, path, size):
        right = pygame.image.load(path).convert_alpha()
        right = pygame.transform.smoothscale(right, size)
        left = pygame.transform.flip(right, True, False)
        return (left, right)
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
        
    def get_position(self):
        return (self.x, self.y)
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        
    def get_size(self):
        return (self.width, self.height)