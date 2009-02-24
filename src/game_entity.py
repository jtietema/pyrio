"""
This file is part of Pyrio.

Pyrio is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pyrio is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pyrio.  If not, see <http://www.gnu.org/licenses/>.
"""
import pygame

from config import Config

class GameEntity():
    # Direction constants
    DIRECTION_RIGHT = 'right'
    DIRECTION_LEFT = 'left'
    
    # Default length of a frame for the sprite animation in milliseconds
    FRAME_LENGTH = 300
    
    def __init__(self, (x,y), (width, height)):
        self.rect = pygame.Rect((x - (width / 2),y - (height / 2)), (width,height))
        self.player = None
        self.config = Config.get_instance()
        
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
    
    def set_player(self, player):
        """Adds a reference to the player object to the entity after the world has been
        initialized."""
        self.player = player
    
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
    
    def collides_with_player(self):
        """Detects if this enemy collides with the player."""
        return self.collide(self.player.get_rect())

    def collidedict(self, dict):
        """Returns (key, value) of the first collision, or None if no collision"""
        return self.rect.collidedict(dict)

    def render_debug(self, screen, (map_x_offset, map_y_offset)):
        if self.config.debug:
            rect_x = self.rect.x - map_x_offset
            rect_y = self.rect.y - map_y_offset
            rect_w = self.rect.width
            rect_h = self.rect.height
            pygame.draw.rect(screen, (255,0,0), (rect_x, rect_y, rect_w, rect_h), 1)
        
