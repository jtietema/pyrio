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
from src.game_entity import GameEntity
from src.states.state import State

class MovingState(State):
    def __init__(*args):
        State.__init__(*args)
    
    def process(self, tick_data):
        """General process function for moving enemies. Returns true if the entity has
        flipped horizontal direction, false if not."""
        x_delta = tick_data['time_passed'] * self.x_speed
        
        heading_left = self.entity.direction is GameEntity.DIRECTION_LEFT
        
        if heading_left:
            x_delta *= -1
        
        # Flip the direction if the requested movement could not be performed.
        if not self.entity.move(x_delta, 0):
            self.entity.direction = GameEntity.DIRECTION_RIGHT if heading_left else GameEntity.DIRECTION_LEFT
            return True
        
        return False