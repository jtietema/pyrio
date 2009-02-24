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

from pygame.locals import *

import src.assets as assets

class StandingState(State):
    def __init__(self, player):
        animations = {
                'left': Animation(assets.images.player, ('stand_left',)),
                'right': Animation(assets.images.player, ('stand_right',))
        }
        State.__init__(self, player, animations, .3, .5)

    def process(self, tick_data):
        # check if falling
        if self.entity.check_falling(tick_data['time_passed'] * self.y_speed):
            return 'falling'

        actions = tick_data['actions']
        if actions.x is not 0:
            return 'walking'
        elif actions.jump:
            return 'jumping'
        else:
            return 'standing'
        