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
import sys

from abstract_menu import AbstractMenu
from video_menu import VideoMenu
from controls_menu import ControlsMenu
from package_menu import PackageMenu
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
            self.submenu = PackageMenu()
            self.submenu.update(tick_data)
        elif index is 1:
            self.submenu = ControlsMenu()
            self.submenu.update(tick_data)
        elif index is 2:
            self.submenu = VideoMenu()
            self.submenu.update(tick_data)
        elif index is 3:
            print 'Bye...'
            sys.exit()
    