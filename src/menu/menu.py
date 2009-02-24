# -*- coding: utf-8 -*-

import sys

from abstract_menu import AbstractMenu
from video_menu import VideoMenu
from controls_menu import ControlsMenu
import src.assets as assets

class Menu(AbstractMenu):
    
    def menu(self):
        self.menu_items = [
            assets.images.menu.start.get_surface(),
            assets.images.menu.controls.get_surface(),
            assets.images.menu.video.get_surface(),
            assets.images.menu.quit.get_surface()
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
    