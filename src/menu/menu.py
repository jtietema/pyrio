# -*- coding: utf-8 -*-

import sys

from abstract_menu import AbstractMenu
from src.asset_manager import AssetManager

class Menu(AbstractMenu):
    
    def menu(self):
        self.menu_items = [
            AssetManager.get_image('menu','start'),
            AssetManager.get_image('menu','quit')
        ]
        self.max_index = 1
    
    def select(self, index, tick_data):
        if index is 0:
            tick_data['pause'] = False
        elif index is 1:
            print 'Bye...'
            sys.exit()
    