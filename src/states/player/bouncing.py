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
from src.states.player.abstract_jumping import AbstractJumpingState

class BouncingState(AbstractJumpingState):
    MAX_JUMPING_TIME = 200
    
    def __init__(self, player):
        AbstractJumpingState.__init__(self, player)
        
        self.name = 'bouncing'
    
    def should_continue_jumping(self, tick_data):
        return self.jumping_time <= BouncingState.MAX_JUMPING_TIME