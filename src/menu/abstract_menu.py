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
import src.assets as assets
from src.overlay import Overlay

class AbstractMenu():
    """Base class for all menu's defines logic for navigating menu's and rendering menu's
    child classes should only define the items and what to do when they get selected.
    
    This means implement the menu() method for defining the menu and the select(index, tick_data)
    method for defining what should happen once an index gets chosen.
    """
    def __init__(self):
        self.index = 0
        self.flower = assets.images.menu.items.flower.get_surface()
        self.screen_size = None
        self.timeout = 300
        self.menu()
        self.max_index = len(self.menu_items) - 1
        self.submenu = None
        
        self.overlay = Overlay(opacity=60)
    
    def update(self, tick_data):
        """Reads the users controls and updates the state from the menu
        If a submenu is present it delegates to the submenu
        """
        actions = tick_data['actions']
        self.screen_size = tick_data['screen_size']
        if self.submenu is not None:
            menu = self.submenu.update(tick_data)
            if menu is None:
                self.submenu = None
                self.timeout = 300
        else:
            # select the current item
            if actions.select and self.timeout is 0:
                self.timeout = 300
                return self.select(self.index, tick_data)
            
            # return to previous menu
            if actions.cancel:
                return None
            
            # select a new menu item
            if actions.y > 0 and self.index is not 0 and self.timeout is 0:
                self.index -= 1
                self.timeout = 300
            if actions.y < 0 and self.index is not self.max_index and self.timeout is 0:
                self.index += 1
                self.timeout = 300
            
            # update timeout, the timeout prevents the menu from operating at insane speeds
            if self.timeout > 0:
                self.timeout -= tick_data['time_passed']
            else:
                self.timeout = 0
        return self
    
    def render(self, screen):
        """If no submenu renders THIS menu otherwise the submenu"""
        if self.submenu is not None:
            self.submenu.render(screen)
        else:
            self.overlay.render(screen)
            
            # define center of the screen to render the menu
            width, height = self.screen_size
            vertical_spacing = height / 8
            width /= 2
            height /= 2
            height -= ((self.max_index + 1) / 2) * vertical_spacing
            
            for index in range(self.max_index + 1):
                image = self.menu_items[index]
                if index is self.index:
                    # draw flower in front of selected item
                    screen.blit(self.flower, (width - 260, height + 20))
                screen.blit(image, (width - 128, height))
                height += vertical_spacing
