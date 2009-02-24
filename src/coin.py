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

from game_locals import *
from game_entity import GameEntity
from animation import Animation

import assets

class Coin(GameEntity):
    def __init__(self, (x,y), map):
        GameEntity.__init__(self, (x,y), (30,30))
        self.map = map
        self.animation = Animation(assets.images.goldpiece.yellow, ('1','2','3','4','5','6','7','8','9','10'))
    
    def update(self, tick_data):
        self.animation.process(tick_data['time_passed'])
        if self.collides_with_player():
            pygame.event.post(pygame.event.Event(COIN_COLLECTED))
            return self
        return None
    
    def render(self, screen, offsets):
        GameEntity.render(self,screen, self.animation.get_image(), offsets)
    