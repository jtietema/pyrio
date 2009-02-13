# -*- coding: utf-8 -*-

import pygame

from abstract_menu import AbstractMenu

class VideoMenu(AbstractMenu):
    def menu(self):
        self.font = pygame.font.SysFont('default', 56)
        self.menu_items = [
            self.font.render('Resolution', True, (200,200,200)),
            self.font.render('Fullscreen', True, (200,200,200)),
            self.font.render('Back', True, (200,200,200))
        ]
    
    def select(self, index, tick_data):
        if index is 2:
            return None
        return self