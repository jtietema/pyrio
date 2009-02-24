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
    # The folder to find the maps in.
    MAPS_FOLDER = 'maps'
    
    def __init__(self, name):
        self.folder = os.path.join(MapPackage.MAPS_FOLDER, name)
        
        config_file = os.path.join(self.folder, 'pkg.cfg')
        lines = open(config_file).read().split('\n')
        
        # Make sure empty lines are filtered out
        self.map_files = filter(None, [line.strip() for line in lines])
        self.current_map_index = 0
    
    def has_next(self):
        """Determines if the package has more maps."""
        return self.current_map_index + 1 < len(self.map_files)
    
    def next(self):
        """Advanced the internal index counter and returns a new world object."""
        if not self.has_next():
            raise Exception("Last map has been reached.")
        else:
            self.current_map_index += 1
        
        return self.current()
    
    def current(self):
        """Creates a new World object based on the current map position."""
        map_file = os.path.join(self.folder, self.map_files[self.current_map_index])
        return World(map_file)