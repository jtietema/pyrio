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
import sys
import os
import re

from game_locals import *
from tile import Tile
from player import Player
from map import Map
from door import Door
import enemies
from coin import Coin

class World():    
    def __init__(self, map_file):
        self.player = None
        self.enemies = []
        self.items = []
        
        self.map = self.deserialize(map_file)
        
        pygame.mixer.music.load(os.path.join('assets', 'music', 'jungle_1.ogg'))
        pygame.mixer.music.play()
        
    def update(self, tick_data):
        self.player.update(tick_data)
        
        for enemy in self.enemies:
            enemy.update(tick_data)
        
        for item in self.items:
            picked_up_item = item.update(tick_data)
            if picked_up_item is not None:
                self.items.remove(picked_up_item)
        
        self.map.update(tick_data)
        
        if self.map.is_finished(self.player):
            pygame.event.post(pygame.event.Event(MAP_FINISHED))
    
    def update_player(self, tick_data):
        """Updates only the player entity."""
        self.player.update(tick_data)
        
    def render(self, screen):
        # Determine map offset
        screen_width, screen_height = screen.get_size()
        x, y = self.player.get_position()

        map_x_offset = x - (screen_width / 2)
        map_y_offset = y - (screen_height / 2)

        map_offsets = (map_x_offset, map_y_offset)
        
        screen.fill((164, 252, 255))
        self.map.render(screen, map_offsets)
        
        for item in self.items:
            item.render(screen, map_offsets)
        
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
        '!': 'pipe_ver',
        '+': 'pipe_up',
        '&': 'stone'
    }

    # The character used to represent the player.
    PLAYER_CHAR = '0'
    
    # The character that represents the door to complete the level.
    DOOR_CHAR = '@'

    # Characters map to the corresponding enemy's class.
    ENEMY_MAP = {
        '1': enemies.Krush,
        '2': enemies.Turtle
    }
    
    ITEM_MAP = {
        '*': Coin
    }
    
    # General settings for tiles. A tile corresponds to one ASCII character in
    # a map file.
    TILE_WIDTH = 64
    TILE_HEIGHT = 64
    
    def deserialize(self, map_file_location):
        """Loads a map from a map configuration file based on the configuration above.
        Returns a fully initialized Map object upon success, raises an Exception and
        returns false in case of an error."""
        map = Map()
        
        # Read the map file
        map_file = open(map_file_location)
        rows = map_file.read().split('\n')
        map_file.close()
        
        # Strip any leading whitespace for the complete map, but only by the minimum
        # amount of whitespace found on any line.
        p = re.compile(r'^(\s*)')
        min_leading_space = min([len(p.match(row).group(1)) for row in rows])
        if min_leading_space > 0:
            rows = [row[min_leading_space:] for row in rows]
        
        # Determine the length of the longest row in the map
        max_length = max([len(row) for row in rows])
        
        # Make sure all rows are padded accordingly, so every row has the same length
        rows = [row.ljust(max_length) for row in rows]
        
        expected_door_coordinates = None

        # We want to insert the entity in the center of the tile space, so divide by two.
        y = World.TILE_HEIGHT / 2
        for row_index, row in enumerate(rows):
            # Again, entity will be placed in the center of the tile space.
            x = World.TILE_WIDTH / 2

            for col_index, char in enumerate(row):
                if char is World.PLAYER_CHAR:
                    if self.player is not None:
                        raise Exception("Player is already placed elsewhere.")
                        return False
                    
                    self.player = Player((x, y), map)
                
                elif char is World.DOOR_CHAR:
                    if expected_door_coordinates is None:
                        expected_door_coordinates = [
                            (x, y),
                            (x + World.TILE_WIDTH, y),
                            (x, y + World.TILE_HEIGHT),
                            (x + World.TILE_WIDTH, y + World.TILE_HEIGHT)
                        ]
                        
                        door = Door((x + World.TILE_WIDTH / 2, y + World.TILE_HEIGHT / 2))
                        map.append_tile(door)
                    elif not (x, y) in expected_door_coordinates:
                        raise Exception("Invalid door location on row %d, column %d." % (row_index, col_index))
                        return False
                    
                elif char in World.ENEMY_MAP:
                    enemy_cls = World.ENEMY_MAP[char]
                    enemy = enemy_cls((x, y), map)
                    self.enemies.append(enemy)
                    
                elif char in World.TILE_MAP:
                    tile_name = World.TILE_MAP[char]
                    if tile_name != None:
                        tile = Tile(tile_name, (x, y))
                        map.append_tile(tile)
                    
                elif char in World.ITEM_MAP:
                    item_cls = World.ITEM_MAP[char]
                    item = item_cls((x,y), map)
                    self.items.append(item)
                
                else:
                    raise Exception('Unknown character on row %d, column %d: %s' % (row_index, col_index, char))
                
                x += World.TILE_WIDTH
                
            y += World.TILE_HEIGHT
        
        if self.player is None:
            raise Exception("No player found in map.")
            return False
        
        # Make sure all the enemies get a reference to the player object for collision
        # detection.
        for enemy in self.enemies:
            enemy.set_player(self.player)
        
        # make sure all items get a reference to the player for collision detection
        for item in self.items:
            item.set_player(self.player)
        
        map.postinit()
        
        return map
        