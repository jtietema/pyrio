# -*- coding: utf-8 -*-

import sys

from abstract_menu import AbstractMenu
from video_menu import VideoMenu
from controls_menu import ControlsMenu
from src.asset_manager import AssetManager

class Menu(AbstractMenu):
    
    def menu(self):
        self.menu_items = [
            AssetManager.get_image('menu','start').get_surface(),
            AssetManager.get_image('menu','controls').get_surface(),
            AssetManager.get_image('menu','video').get_surface(),
            AssetManager.get_image('menu','quit').get_surface()
        ]
    
    def select(self, index, tick_data):
        if index is 0:
            tick_data['pause'] = False
        elif index is 1:
            self.submenu = ControlsMenu()
            self.submenu.update(tick_data)
        elif index is 2:
            self.submenu = VideoMenu()
            self.submenu.update(tick_data)
        elif index is 3:
            print 'Bye...'
            sys.exit()
    