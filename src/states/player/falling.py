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
from src.states.state import State
from src.animation import Animation
from src.game_entity import GameEntity

from pygame.locals import *

class FallingState(State):
    
    def __init__(self, player):
        animations = {
            'left' : Animation('player', ('fall_left', )),
            'right': Animation('player', ('fall_right',))
        }
        State.__init__(self, player, animations, .3, .5)

    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        actions = tick_data['actions']

        y_delta = time_passed * self.y_speed
        
        # check if still falling
        if not self.entity.check_falling(time_passed * self.y_speed):
            # check if we really can't fall another pixel
            y_delta = int(time_passed * self.y_speed)
            while y_delta > 0:
                y_delta -= 1
                if self.entity.check_falling(y_delta):
                    break
            
            if y_delta is 0:
                if actions.x is not 0:
                    return 'walking'
                else:
                    return 'standing'

        # continue falling
        x_delta = self.x_speed * time_passed * actions.x
        if actions.x < 0:
            self.entity.direction = GameEntity.DIRECTION_LEFT
        elif actions.x > 0:
            self.entity.direction = GameEntity.DIRECTION_RIGHT
        else:
            x_delta = 0

        self.entity.move(x_delta, y_delta)
        return 'falling'
