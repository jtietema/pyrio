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

from abstract_menu import AbstractMenu
from src.config import Config
from src.game_locals import *

class ResolutionMenu(AbstractMenu):
    def menu(self):
        self.modes = pygame.display.list_modes(32)
        self.menu_items = []
        self.font = pygame.font.SysFont('sans', 48)
        for mode in self.modes:
            self.menu_items.append(self.font.render(str(mode[0]) + 'x' + str(mode[1]), True, (200,200,200)))
        self.menu_items.append(self.font.render('Back', True, (200,200,200)))
    
    def select(self, index, tick_data):
        # back is selected
        if index is len(self.modes):
            return None
        # else resolution is selected
        config = Config.get_instance()
        config.set_resolution(self.modes[index])
        config.write()
        pygame.event.post(pygame.event.Event(VIDEOMODE_CHANGED))