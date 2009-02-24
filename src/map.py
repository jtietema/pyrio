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
from pygame.locals import *

from door import Door

class Map():
    TILE_WIDTH = 64
    TILE_HEIGHT = 64
    
    def __init__(self):
        self.tiles = []
        
        self.door = None
        
        self.x_offset = 0
        self.y_offset = 0
        
    def postinit(self):
        """Automatically called by deserialize() method in World, after all tiles have
        been loaded. This sets some meta information about the map and initiates
        building of the tile matrix."""
        self.width = max([tile.get_left() + tile.get_width() for tile in self.tiles])
        self.height = max([tile.get_top() + tile.get_height() for tile in self.tiles])
        
        self.build_tile_matrix()
    
    def build_tile_matrix(self):
        """Builds a matrix from all the tiles that have been appended. This matrix is used
        for quick lookup of certain tile objects, which in turn can be used to speed up
        collision detection with the map by eliminating most objects from the comparison.
        The tile matrix only contains tiles the player can collide with (since collisions
        are the sole purpose of its existance), so the Door object is ommited.
        """
        num_rows = self.height / Map.TILE_HEIGHT
        num_columns = self.width / Map.TILE_WIDTH
        
        # Fill the tile matrix with None objects. Make sure the matrix's rows are copies
        # of, instead of references to, the initial empty row.
        empty_row = [None] * num_columns
        self.tile_matrix = []
        for row_index in xrange(num_rows):
            self.tile_matrix.insert(row_index, empty_row[:])
        
        for tile in self.tiles:
            x, y = tile.get_rect().topleft
            row = y // Map.TILE_HEIGHT
            column = x // Map.TILE_WIDTH
            
            # Make sure the position we calculated is not occupated yet.
            assert self.tile_matrix[row][column] is None
            
            self.tile_matrix[row][column] = tile
    
    def update(self, tick_data):
        pass
        
    def render(self, screen, map_offsets):
        """Renders all the tiles on the map. Also renders the Door if one is available."""
        screen_width, screen_height = screen.get_size()
        
        for tile in self.tiles:
            tile.render(screen, map_offsets)
        
        if self.door is not None:
            self.door.render(screen, map_offsets)
                    
    def collisions(self, game_entity, (delta_x, delta_y)):
        """Returns true if the supplied game entity has collisions with any tiles
        or boundaries on the map. This also includes checks for map start and end
        boundaries. Since this method is mostly used to check the validity of a requested
        movement, the delta position needs to be supplied instead of a full position."""
        new_rect = game_entity.get_rect().move(delta_x, delta_y)
        
        # Check for map boundaries.
        if new_rect.left < 0 or new_rect.right + new_rect.width > self.width:
            return True
        
        # Fetch some information from the target rect of the entity.
        x, y = new_rect.topleft
        w, h = new_rect.size
        
        # Determine what part of the matrix to check for collisions.
        start_row_index, start_col_index = (max(0, y // Map.TILE_HEIGHT), max(0, x // Map.TILE_WIDTH))
        end_row_index = max(0, min(y + h, self.height) // Map.TILE_HEIGHT)
        end_col_index = max(0, min(x + w, self.width) // Map.TILE_WIDTH)
        
        for row_index in xrange(start_row_index, end_row_index + 1):            
            for col_index in xrange(start_col_index, end_col_index + 1):                
                tile = self.tile_matrix[row_index][col_index]
                if tile is not None and tile.collide(new_rect):
                    return True
        
        return False
    
    def is_finished(self, player):
        """Returns true if the player has completed the map."""
        if self.door is not None:
            return self.door.get_rect().contains(player.get_rect())
        return False
    
    def append_tile(self, tile):
        """Appends the tile to the appropriate list. We split the map's door from
        the tiles to prevent expensive isinstance calls on every cycle."""
        if isinstance(tile, Door):
            self.door = tile
        else:
            self.tiles.append(tile)
