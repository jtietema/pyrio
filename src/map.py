
from pygame.locals import *

from door import Door

class Map():
    def __init__(self):
        self.tiles = []
        
        self.door = None
        
        self.x_offset = 0
        self.y_offset = 0
        
    def postinit(self):
        """Automatically called by deserialize() method in World, after all tiles have
        been loaded. This sets some meta information about the map."""
        self.width = max([tile.get_x() + tile.get_width() for tile in self.tiles])
        self.height = max([tile.get_y() + tile.get_height() for tile in self.tiles])
    
    def update(self, tick_data):
        pass
        
    def render(self, screen, offsets):
        screen_width, screen_height = screen.get_size()
        
        for tile in self.tiles:
            tile.render(screen, offsets)
                    
    def collisions(self, game_entity, (delta_x, delta_y)):        
        new_rect = game_entity.get_rect().move(delta_x, delta_y)
        
        if new_rect.left < 0 or new_rect.right + new_rect.width > self.width:
            return True
                
        for tile in self.tiles:
            if not isinstance(tile, Door) and tile.collide(new_rect):
                return True
        return False
    
    def is_finished(self, player):
        if self.door is not None:
            return self.door.get_rect().contains(player.get_rect())
        return False
    
    def append_tile(self, tile):
        if isinstance(tile, Door):
            self.door = tile
        
        self.tiles.append(tile)
