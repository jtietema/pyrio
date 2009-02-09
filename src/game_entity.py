
import pygame

class GameEntity():
    # Direction constants
    DIRECTION_RIGHT = 1
    DIRECTION_LEFT = 0
    
    # Length of a frame for the sprite animation in milliseconds
    FRAME_LENGTH = 300
    
    def __init__(self, (x,y), (width, height)):
        self.rect = pygame.Rect((x - (width / 2),y - (height / 2)), (width,height))

        
    def get_x(self):
        return self.rect.centerx
    
    def get_y(self):
        return self.rect.centery
        
    def get_position(self):
        return (self.rect.centerx, self.rect.centery)
    
    def get_width(self):
        return self.rect.width
    
    def get_height(self):
        return self.rect.height
        
    def get_size(self):
        return (self.rect.width, self.rect.height)

    def get_rect(self):
        return self.rect
    
    def render(self, screen, image, (x, y)):
        x -= (image.get_width() / 2)
        y -= (image.get_height() / 2)
        screen.blit(image, (x, y))

    def collide(self, rect):
        """Returns a boolean if the to rects collide"""
        return self.rect.colliderect(rect)

    def collidedict(self, dict):
        """Returns (key, value) of the first collision, or None if no collision"""
        return self.rect.collidedict(dict)
        
