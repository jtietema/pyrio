
import os
from random import randint

from tile import Tile
from player import Player
from map import Map
import enemies

class World():    
    def __init__(self):
        self.player = None
        self.enemies = []
        
        self.map = self.deserialize('test')
        
    def update(self, tick_data):
        for enemy in self.enemies:
            enemy.update(tick_data)
        
        self.player.update(tick_data)
        
        self.map.update(tick_data)
        
    def render(self, screen):
        # Determine map offset
        screen_width, screen_height = screen.get_size()
        x, y = self.player.get_position()

        map_x_offset = x - (screen_width / 2)
        map_y_offset = y - (screen_height / 2)

        map_offsets = (map_x_offset, map_y_offset)
        
        screen.fill((164, 252, 255))
        self.map.render(screen, map_offsets)
        
        for enemy in self.enemies:
            enemy.render(screen, map_offsets)
        
        self.player.render(screen)
    
        
    # The folder to find the maps in.
    MAPS_FOLDER = 'maps'

    # Characters map to tile images.
    TILE_MAP = {
        ' ': None,
        '-': 'up',
        '#': 'middle',
        '<': 'left',
        '>': 'right',
        '/': 'left_up',
        '\\': 'right_up',
        '`': 'pipe_ver',
        '~': 'pipe_up'
    }

    # The character used to represent the player.
    PLAYER_CHAR = '0'

    # Characters map to the corresponding enemy's class.
    ENEMY_MAP = {
        '1': 'Krush',
        '2': 'Turtle'
    }
    
    # General settings for tiles. A tile corresponds to one ASCII character in
    # a map file.
    TILE_WIDTH = 64
    TILE_HEIGHT = 64
    
    def deserialize(self, name):
        """Loads a map from a map configuration file based on the configuration above.
        Returns a fully initialized Map object upon success, raises an Exception and
        returns false in case of an error."""
        map = Map()
        
        # Read the map file
        map_file = open(os.path.join(World.MAPS_FOLDER, name + '.map'))
        rows = map_file.read().split('\n')
        map_file.close()
        
        # TODO: strip leading and trailing white space
        
        # Determine the length of the longest row in the map
        max_length = max([len(row) for row in rows])
        
        # Make sure all rows are padded accordingly, so every row has the same length
        # rows = [row.ljust(max_length) for row in rows]

        # We want to insert the entity in the center of the tile space, so divide by two.
        y = World.TILE_HEIGHT / 2
        for row_index, row in enumerate(rows):            
            # Again, entity will be placed in the center of the tile space.
            x = World.TILE_WIDTH / 2

            for col_index, char in enumerate(row):
                if char is World.PLAYER_CHAR:
                    if self.player is not None:
                        raise Exception("Player is already on the map.")
                        return False
                    
                    self.player = Player((x, y), map)
                    
                elif char in World.ENEMY_MAP:
                    enemy_cls = globals()['enemies'].__dict__[World.ENEMY_MAP[char]]
                    enemy = enemy_cls((x, y), map)
                    self.enemies.append(enemy)
                    
                elif char in World.TILE_MAP:
                    tile_name = World.TILE_MAP[char]
                    if tile_name != None:
                        tile = Tile(tile_name, (x, y))
                        map.append_tile(tile)
                
                else:
                    raise Exception('Unknown character on row %d, column %d: %s' % (row_index, col_index, char))
                
                x += World.TILE_WIDTH
                
            y += World.TILE_HEIGHT
        
        if self.player is None:
            raise Exception("No player found in map.")
            return False
        
        map.postinit()
        
        return map
        