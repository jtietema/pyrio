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
from pygame.locals import *
from src.game_locals import *

from src.game_states.game_state import GameState

class PlayerDeathState(GameState):
    def update(self, tick_data):
        next_state = 'player_death'
        
        for event in self.get_events():
            if event.type == DEATH_ANIMATION_DONE:
                self.game.lives -= 1
                
                # Reset the world.
                self.game.reset_world()
                
                next_state = 'playing'
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    next_state = 'paused'
        
        self.game.world.update_player(tick_data)
        self.game.hud.update(tick_data)
        
        return next_state