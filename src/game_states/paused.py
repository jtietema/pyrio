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
from pygame.locals import *

from src.game_states.game_state import GameState
from src.menu.menu import Menu

class PausedState(GameState):
    """State for paused games. This stops updating the positions of the game entities
    and disables control of the player character. This also renders a menu over the
    paused World."""
    
    def __init__(self, *args):
        GameState.__init__(self, *args)
        
        # Assume the previous state is playing if none is set explicitly.
        self.previous_state = 'playing'
    
    def update(self, tick_data):
        next_state = 'paused'
        
        for event in self.get_events():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    next_state = self.previous_state
        
        self.menu.update(tick_data)
        
        return next_state
    
    def render(self, screen):        
        GameState.render(self, screen)
        
        # Render the menu over the world and the hud.
        self.menu.render(screen)
        
    def enter(self, previous_state):
        """Creates a new Menu object."""
        self.menu = Menu()
        pygame.mixer.pause()
        self.previous_state = previous_state
    
    def exit(self, next_state):
        """Destroys the menu object."""
        del self.menu
        pygame.mixer.unpause()