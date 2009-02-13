# -*- coding: utf-8 -*-

from abstract_menu import AbstractMenu

class ControlsMenu(AbstractMenu):
    def menu(self):
        self.menu_items = []
    
    def select(self, index, tick_data):
        pass