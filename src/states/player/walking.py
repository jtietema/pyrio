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

class WalkingState(State):

    def __init__(self, player):
        animations = {
            'left': Animation('player', ('walk_left_1', 'walk_left_2'), 200),
            'right': Animation('player', ('walk_right_1', 'walk_right_2'), 200)
        }
        State.__init__(self, player, animations, .3, .5)

    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        actions = tick_data['actions']
        x_delta = time_passed * self.x_speed * actions.x

        next_state = 'walking'

        # check if falling
        if self.entity.check_falling(time_passed * self.y_speed):
            return 'falling'

        # process walking
        if actions.x < 0:
            self.entity.direction = GameEntity.DIRECTION_LEFT
        elif actions.x > 0:
            self.entity.direction = GameEntity.DIRECTION_RIGHT
        else:
            x_delta = 0
            next_state = 'standing'

        # check if jumping
        if actions.jump:
            next_state = 'jumping'

        self.entity.move(x_delta, 0)

        return next_state
