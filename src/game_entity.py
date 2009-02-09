
import pygame

class GameEntity():
    # Direction constants
    DIRECTION_RIGHT = 1
    DIRECTION_LEFT = 0
    
    # Length of a frame for the sprite animation in milliseconds
    FRAME_LENGTH = 300
    
    def __init__(self, (x,y), (width, height)):
        # Position
        self.x = x
        self.y = y
        
        # Size
        self.width = width
        self.height = height
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
        
    def get_position(self):
        return (self.x, self.y)
    
    def get_real_position(self):
        return (self.x - (self.width / 2), self.y - (self.height / 2))
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
        
    def get_size(self):
        return (self.width, self.height)
    
    def render(self, screen, image, (x, y)):
        x -= (image.get_width() / 2)
        y -= (image.get_height() / 2)
        screen.blit(image, (x, y))
        
    def collision(self, (x,y), (delta_x, delta_y)):
        """Detects if the given move will result in a collision with this object. It 
        returns the possible delta (if no collision returns original delta's)
        """
        distance_x = abs(self.x - x) - (self.width / 2)
        distance_y = abs(self.y - y) - (self.height / 2)
        
        if (distance_x < delta_x) and (distance_y < delta_y):
            delta_x = distance_x
            delta_y = distance_y
        return (delta_x, delta_y)
