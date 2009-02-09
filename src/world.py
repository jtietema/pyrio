
import os

from tile import Tile
from player import Player
from map import Map
from enemy import Enemy

class World():
    MAPS_FOLDER = 'maps'
    
    # Characters map to tile images
    TILE_MAP = {
        ' ': None,
        '-': 'up',
        '#': 'middle',
        '<': 'left',
        '>': 'right',
        '/': 'left_up',
        '\\': 'right_up'
    }
    
    # The character used to represent the player
    PLAYER_CHAR = '0'

    # Characters map to the enemy's class
    ENEMY_MAP = {
        '1': 'Enemy'
    }

    TILE_WIDTH = 64
    TILE_HEIGHT = 64
    
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
    
    def deserialize(self, name):
        map = Map()
        
        # Read the map file
        map_file = open(os.path.join(World.MAPS_FOLDER, name + '.map'))
        rows = map_file.read().split('\n')
        map_file.close()

        max_length = max([len(row) for row in rows])
        rows = [row.ljust(max_length) for row in rows]

        tiles = []
        y = World.TILE_HEIGHT / 2
        for row_index, row in enumerate(rows):
            x = World.TILE_WIDTH / 2

            for col_index, char in enumerate(row):
                if char is World.PLAYER_CHAR:
                    self.player = Player((x, y), map)
                    
                elif char in World.ENEMY_MAP:
                    enemy_cls = globals()[World.ENEMY_MAP[char]]
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
        
        map.postinit()
        
        return map
        