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
from src.animation import Animation
from src.states.enemies.moving import MovingState

import src.assets as assets

class FlatState(MovingState):
    def __init__(self, enemy):
        animations = {
            'left': Animation(assets.images.enemies.krush, ('flat_left_1', 'flat_left_2', 'flat_left_3'), 100),
            'right': Animation(assets.images.enemies.krush, ('flat_right_1', 'flat_right_2', 'flat_right_3'), 100)
        }
        
        self.counter = 0
        self.max_flat_time = 5000
        
        MovingState.__init__(self, enemy, animations, .1, 0)
    
    def process(self, tick_data):        
        MovingState.process(self, tick_data)
        
        self.counter += tick_data['time_passed']
        
        if self.counter > self.max_flat_time:
            return 'walk'
        
        if self.entity.collides_with_player():
            if self.entity.is_hit_by_player():
                self.entity.bounce_player(tick_data)
                self.counter = 0
        
        return 'flat'
    
    def enter(self):
        MovingState.enter(self)
        
        self.counter = 0
        self.entity.rect.size = (60, 44)
        self.entity.rect.move_ip(0, 8)
    
    def exit(self):
        MovingState.exit(self)
        
        self.entity.rect.size = self.entity.default_size
        self.entity.rect.move_ip(0, -8)