
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
        
    def collision(self, (x,y), (delta_x, delta_y)):
        """Detects if the given move will result in a collision with this object. It 
        returns the possible delta (if no collision returns original delta's)
        """
        new_delta_x = delta_x
        new_delta_y = delta_y
        distance_x = abs((self.x - x) - (self.width / 2))
        distance_y = abs((self.y - y) - (self.height / 2))
        
        if (distance_x < abs(delta_x)) and distance_y < (self.height/2):
            new_delta_x = distance_x
        if (distance_y < abs(delta_y)) and distance_x < (self.width/2):
            new_delta_y = distance_y
        return (new_delta_x, new_delta_y)
        