
import pygame

class GameEntity():
    def __init__(self, (x,y), (width, height), map):
        # position
        self.x = x
        self.y = y
        
        # size
        self.width = width
        self.height = height
        
        self.map = map
    
    def load_twodirectional_asset(self, path, size):
        right = pygame.image.load(path).convert_alpha()
        right = pygame.transform.smoothscale(right, size)
        left = pygame.transform.flip(right, True, False)
        return (left, right)
        
    def get_position(self):
        return (self.x, self.y)
        
    def get_size(self):
        return (self.width, self.height)
        
    def collision(self, (x,y), (delta_x, delta_y)):
        """Detects if the given move will result in a collision with this object. It 
        returns the possible delta (if no collision returns original delta's)
        """
        distance_x = abs(self.x - x) - (self.width / 2)
        distance_y = abs(self.y - y) - (self.height / 2)
        
        if distance_x < delta_x:
            delta_x = distance_x
        if distance_y < delta_y:
            delta_y = distance_y
        return (delta_x, delta_y)
        