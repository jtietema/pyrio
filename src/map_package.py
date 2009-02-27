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

from ConfigParser import RawConfigParser
import os

from world import World

class MapPackage():
    """Represents a map package. A map package consits of .map files specifying the
    layout of the maps, a pkg.cfg specifying which maps are available with additional
    options such as music, and a maps.list file specifying the order of the maps in the
    package."""
    
    # The folder to find the map packages in.
    MAPS_FOLDER = 'maps'
    
    def __init__(self, name):
        self.folder = os.path.join(MapPackage.MAPS_FOLDER, name)
        
        self.load_config()
        
        list_file = os.path.join(self.folder, 'maps.list')
        lines = open(list_file).read().split('\n')
        
        # Make sure empty lines are filtered out
        self.maps = filter(None, [line.strip() for line in lines])
        
        self.current_map_index = 0
    
    def load_config(self):
        """Loads the config file for this map package. Simply adds a reference
        to the RawConfigParser object as an attribute to this object."""
        config_file = os.path.join(self.folder, 'pkg.cfg')
        self.config = RawConfigParser()
        self.config.read(config_file)
    
    def has_next(self):
        """Determines if the package has more maps."""
        return self.current_map_index + 1 < len(self.maps)
    
    def next(self):
        """Advanced the internal index counter and returns a new world object."""
        if not self.has_next():
            raise Exception("Last map has been reached.")
        else:
            self.current_map_index += 1
        
        return self.current()
    
    def current(self):
        """Creates a new World object based on the current map position. Also passes
        along additional options to the World constructor as a dictionary."""
        map_name = self.maps[self.current_map_index]
        options = dict(self.config.items(map_name))
        map_file = os.path.join(self.folder, options.pop('file'))
        return World(map_file, options)