
import os

from tile import Tile

class MapSerializer():
    maps_folder = 'maps'
    
    char_map = {
        ' ': None,
        '_': 'up',
        '#': 'middle'
    }
    
    tile_width = 64
    tile_height = 64
    
    @classmethod
    def deserialize(cls, name):
        # Read in the map file
        map_file = open(os.path.join(cls.maps_folder, name + '.map'))
        rows = map_file.read().split('\n')
        map_file.close()
        
        max_length = max([len(row) for row in rows])
        rows = [row.ljust(max_length) for row in rows]
        
        tiles = []
        y = 0
        for row_index, row in enumerate(rows):
            x = 0
            
            for col_index, char in enumerate(row):
                if not cls.char_map.has_key(char):
                    raise Exception('Unknown tile charachter on row %d, column %d: %s' % row_index, col_index, char)
                    
                tile_name = cls.char_map[char]
                if tile_name != None:
                    tile = Tile(tile_name, (x, y))
                    tiles.append(tile)
                
                x += cls.tile_width
                
            y += cls.tile_height
        
        return tiles