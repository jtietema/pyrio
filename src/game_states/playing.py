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
from src.config import Config

class PlayingState(GameState):
    """State to represent a game that is currently active, allowing for user interaction
    with the player entity.
    """
    
    def __init__(self, *args):
        GameState.__init__(self, *args)
        
        self.debug = False
    
    def update(self, tick_data):
        next_state = 'playing'
        
        for event in self.get_events():
            if event.type == PLAYER_DEATH:
                next_state = 'player_death'
            elif event.type == MAP_FINISHED:
                next_state = 'map_transition'
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    config = Config.get_instance()
                    if config.debug:
                        config.debug = False
                    else:
                        config.debug = True
                if event.key == K_r:
                    self.game.reset_world()
                if event.key == K_ESCAPE and next_state is 'playing':
                    next_state = 'paused'
        
        tick_data['debug'] = self.debug
        
        self.game.world.update(tick_data)
        self.game.hud.update(tick_data)
        
        return next_state