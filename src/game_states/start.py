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
from src.game_locals import *

class StartState(GameState):
        
    def update(self, tick_data):
        for event in self.get_events():
            if event.type == MAP_PACKAGE_SELECTED:
                self.menu = None
        if self.menu is not None:
            self.menu.update(tick_data)
        return 'start'
    
    def render(self, screen):        
        # Render only the menu.
        self.menu.render(screen)
        
    def enter(self, previous_state):
        """Creates a new Menu object."""
        self.menu = Menu()
    
    def exit(self, next_state):
        """Destroys the menu object."""
        del self.menu
