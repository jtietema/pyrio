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

class WalkingState(MovingState):
    def __init__(self, enemy):
        animations = {
            'left': Animation(assets.images.enemies.turtle, ('walk_left_1', 'walk_left_2', 'walk_left_3'), 200),
            'right': Animation(assets.images.enemies.turtle, ('walk_right_1', 'walk_right_2', 'walk_right_3'), 200)
        }
        
        MovingState.__init__(self, enemy, animations, .15, 0)
    
    def process(self, tick_data):
        MovingState.process(self, tick_data)

        if self.entity.collides_with_player():
            if self.entity.is_hit_by_player():
                self.entity.bounce_player(tick_data)
                return 'shell'

            self.entity.hit_player(tick_data)

        return 'walk'