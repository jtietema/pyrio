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
import os

import pygame

from abstract_menu import AbstractMenu
from src.game_locals import *

class PackageMenu(AbstractMenu):
    def menu(self):
        self.font = pygame.font.SysFont('default', 48)
        self.paks = os.listdir(os.path.join('.', 'maps'))
        self.menu_items = []
        for pak in self.paks:
            self.menu_items.append(self.font.render(pak, True, (200,200,200)))
        self.menu_items.append(self.font.render('Back', True, (200,200,200)))
    
    def select(self, index, tick_data):
        # back is selected
        if index is len(self.paks):
            return None
        # else map package selected
        pygame.event.post(pygame.event.Event(MAP_PACKAGE_SELECTED, map_package=self.paks[index]))
        tick_data['pause'] = False
