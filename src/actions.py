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
from pygame.locals import *

from config import Config

class Actions():
    """
    Simple class to hold all the actions the player can do.  In the rest of the game you
    are suppossed to use this class instead off reading the controls directly.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.jump = False
        self.select = False
        self.cancel = False
        self.joystick = None
        
        # setup joystick/gamepad if present
        joystick = None
        if pygame.joystick.get_count() > 0:
            # at least one joystick is found
            print str(pygame.joystick.get_count()) + ' joystick(s) found'
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print 'Joystick found with ' + str(self.joystick.get_numaxes()) + \
             ' axes and ' + str(self.joystick.get_numbuttons()) + ' buttons'

    def set_x(self, x):
        """Must be a float between 1 (right) and -1 (left)"""
        self.x = x

    def set_y(self, y):
        """Must be a float between 1 (up) and -1 (down)"""
        self.y = y

    def set_jump(self, boolean):
        self.jump = boolean

    def reset(self):
        self.__init__()

    def set_select(self, boolean):
        self.select = True
    
    def set_cancel(self, boolean):
        self.cancel = True
    
    def process_controls(self):
        """
        Maps all the supported controls to a common format.
        """
        config = Config.get_instance()
        self.reset()
        # process the keyboard controls
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[config.get_key('up')]:
            self.set_jump(True)

        if pressed_keys[config.get_key('left')]:
            self.set_x(-1.0)

        if pressed_keys[config.get_key('right')]:
            self.set_x(1.0)

        if pressed_keys[config.get_key('up')]:
            self.set_y(1.0)

        if pressed_keys[config.get_key('down')]:
            self.set_y(-1.0)

        if pressed_keys[config.get_key('select')]:
            self.set_select(True)
        
        if pressed_keys[config.get_key('cancel')]:
            self.set_cancel(True)

        # process gamepad / joystick
        if self.joystick is not None:
            if self.joystick.get_button(0):
                self.set_jump(True)
            if self.joystick.get_button(1):
                self.set_select(True)
            if self.joystick.get_axis(0) > .05 or self.joystick.get_axis(0) < -.05:
                self.set_x(self.joystick.get_axis(0))
            if self.joystick.get_axis(1) > .05 or self.joystick.get_axis(1) < -.05:
                self.set_y(-1 * self.joystick.get_axis(1))
        
        return self
        