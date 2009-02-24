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
from src.game_locals import *

from src.config import Config

from abstract_menu import AbstractMenu
from resolution_menu import ResolutionMenu

class VideoMenu(AbstractMenu):
    def menu(self):
        config = Config.get_instance()
        if config.get_fullscreen():
            fullscreen = 'Fullscreen'
        else:
            fullscreen = 'Windowed'
        if config.get_hardwareacceleration():
            hardwareacceleration = 'Hardware acceleration'
        else:
            hardwareacceleration = 'Software rendering'
        if config.get_doublebuffer():
            doublebuffer = 'Doublebuffer: on'
        else:
            doublebuffer = 'Doublebuffer: off'
        self.font = pygame.font.SysFont('default', 56)
        self.menu_items = [
            self.font.render('Resolution', True, (200,200,200)),
            self.font.render(fullscreen, True, (200,200,200)),
            self.font.render(hardwareacceleration, True, (200,200,200)),
            self.font.render(doublebuffer, True, (200,200,200)),
            self.font.render('Back', True, (200,200,200))
        ]
    
    def select(self, index, tick_data):
        config = Config.get_instance()
        if index is 0:
            self.submenu = ResolutionMenu()
            self.submenu.update(tick_data)
        if index is 1:
            if config.get_fullscreen():
                fullscreen = 'Windowed'
                config.set_fullscreen(False)
            else:
                fullscreen = 'Fullscreen'
                config.set_fullscreen(True)
            config.write()
            self.menu_items[1] = self.font.render(fullscreen, True, (200,200,200))
            pygame.event.post(pygame.event.Event(VIDEOMODE_CHANGED))
        if index is 2:
            if config.get_hardwareacceleration():
                hardwareacceleration = 'Software rendering'
                config.set_hardwareacceleration(False)
            else:
                hardwareacceleration = 'Hardware acceleration'
                config.set_hardwareacceleration(True)
            config.write()
            self.menu_items[2] = self.font.render(hardwareacceleration, True, (200,200,200))
            pygame.event.post(pygame.event.Event(VIDEOMODE_CHANGED))
        if index is 3:
            if config.get_doublebuffer():
                doublebuffer = 'Doublebuffer: off'
                config.set_doublebuffer(False)
            else:
                config.set_doublebuffer(True)
                doublebuffer = 'Doublebuffer: on'
            config.write()
            self.menu_items[3] = self.font.render(doublebuffer, True, (200,200,200))
            pygame.event.post(pygame.event.Event(VIDEOMODE_CHANGED))
        if index is 4:
            return None
        return self
    