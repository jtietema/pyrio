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
from game_entity import GameEntity
from asset_manager import AssetManager

class Tile(GameEntity):
    def __init__(self, name, (x, y)):
        self.image = AssetManager.get_image('map', name)
        
        GameEntity.__init__(self, (x, y), self.image.get_size())
    
    def render(self, screen, offsets):
        GameEntity.render(self, screen, self.image, offsets)