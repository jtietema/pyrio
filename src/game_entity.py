
import pygame

class GameEntity():
    # Direction constants
    DIRECTION_RIGHT = 'right'
    DIRECTION_LEFT = 'left'
    
    # Default length of a frame for the sprite animation in milliseconds
    FRAME_LENGTH = 300
    
    def __init__(self, (x,y), (width, height)):
        self.rect = pygame.Rect((x - (width / 2),y - (height / 2)), (width,height))
        self.debug = False
        
    def get_x(self):
        return self.rect.centerx
    
    def get_y(self):
        return self.rect.centery
    
    def get_top(self):
        return self.rect.top
    
    def get_left(self):
        return self.rect.left
        
    def get_position(self):
        return (self.rect.centerx, self.rect.centery)
    
    def get_width(self):
        return self.rect.width
    
    def get_height(self):
        return self.rect.height
        
    def get_size(self):
        return (self.rect.width, self.rect.height)
    
    def set_size(self, size):
        self.rect.size = size

    def get_rect(self):
        return self.rect
    
    def render(self, screen, image, (map_x_offset, map_y_offset)):
        """Renders the entity when it is in the visible area of the map."""
        width, height = self.get_size()
        
        x_screen = self.rect.x - map_x_offset
        y_screen = self.rect.y - map_y_offset
    
        if ((x_screen + width > 0 or x_screen < width) and (y_screen + height > 0 or y_screen < height)):
            offset_x, offset_y = image.get_offset()
            screen.blit(image.get_surface(), (x_screen + offset_x, y_screen + offset_y))
            self.render_debug(screen, (map_x_offset, map_y_offset))

    def collide(self, rect):
        """Returns a boolean if the two rects collide"""
        return self.rect.colliderect(rect)

    def collidedict(self, dict):
        """Returns (key, value) of the first collision, or None if no collision"""
        return self.rect.collidedict(dict)

    def render_debug(self, screen, (map_x_offset, map_y_offset)):
        if self.debug:
            rect_x = self.rect.x - map_x_offset
            rect_y = self.rect.y - map_y_offset
            rect_w = self.rect.width
            rect_h = self.rect.height
            pygame.draw.rect(screen, (255,0,0), (rect_x, rect_y, rect_w, rect_h), 1)
        
