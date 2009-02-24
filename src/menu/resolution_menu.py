import pygame

from abstract_menu import AbstractMenu
from src.config import Config
from src.game_locals import *

class ResolutionMenu(AbstractMenu):
    def menu(self):
        self.modes = pygame.display.list_modes(32)
        self.menu_items = []
        self.font = pygame.font.SysFont('default', 48)
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