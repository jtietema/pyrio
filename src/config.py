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
import os
import ConfigParser

import pygame
from pygame.locals import *


class Config():
    _instance = None
    
    def __init__(self):
        display_info = pygame.display.Info()
        self.resolution = (display_info.current_w, display_info.current_h)
        self.fullscreen = False
        self.hardwareacceleration = False
        self.doublebuffer = False
        self.keys = {
                     'up'       : K_UP,
                     'down'     : K_DOWN,
                     'left'     : K_LEFT,
                     'right'    : K_RIGHT,
                     'cancel'   : K_ESCAPE,
                     'select'   : K_RETURN
                     }
        self.settings_file = os.path.join(os.path.expanduser("~"), '.pyrio')
        self.settings = None
        self.load_config()
    
    def set_resolution(self, resolution):
        self.resolution = resolution
    
    def get_resolution(self):
        return self.resolution
    
    def get_key(self, action):
        return self.keys[action]
    
    def set_key(self, action, key):
        self.keys[action] = key
    
    def get_fullscreen_bitwise(self):
        if self.fullscreen:
            return FULLSCREEN
        else:
            return 0
    
    def get_fullscreen(self):
        return self.fullscreen
        
    def set_fullscreen(self, fullscreen):
        self.fullscreen = fullscreen
    
    def get_doublebuffer_bitwise(self):
        if self.doublebuffer:
            return DOUBLEBUF
        else:
            return 0
    
    def get_doublebuffer(self):
        return self.doublebuffer
    
    def set_doublebuffer(self, doublebuffer):
        self.doublebuffer = doublebuffer
    
    def get_hardwareacceleration_bitwise(self):
        if self.hardwareacceleration:
            return HWSURFACE
        else:
            return 0
    
    def get_hardwareacceleration(self):
        return self.hardwareacceleration
    
    def set_hardwareacceleration(self, hardwareacceleration):
        self.hardwareacceleration = hardwareacceleration
    
    def load_config(self):
        self.settings = ConfigParser.RawConfigParser()
        self.settings.read(self.settings_file)
        
        # read screen options
        if self.settings.has_section('screen'):
            if self.settings.has_option('screen','height'):
                self.resolution = (self.resolution[0], self.settings.getint('screen', 'height'))
            if self.settings.has_option('screen', 'width'):
                self.resolution = (self.settings.getint('screen', 'width'), self.resolution[1])
            if self.settings.has_option('screen', 'fullscreen'):
                self.fullscreen = self.settings.getboolean('screen', 'fullscreen')
            if self.settings.has_option('screen', 'hardwareacceleration'):
                self.hardwareacceleration = self.settings.getboolean('screen', 'hardwareacceleration')
            if self.settings.has_option('screen', 'doublebuffer'):
                self.doublebuffer = self.settings.getboolean('screen', 'doublebuffer')
        
        # read controls
        if self.settings.has_section('controls'):
            if self.settings.has_option('controls', 'up'):
                self.keys['up'] = self.settings.getint('controls', 'up')
            if self.settings.has_option('controls', 'down'):
                self.keys['down'] = self.settings.getint('controls', 'down')
            if self.settings.has_option('controls', 'left'):
                self.keys['left'] = self.settings.getint('controls', 'left')
            if self.settings.has_option('controls', 'right'):
                self.keys['right'] = self.settings.getint('controls', 'right')
            if self.settings.has_option('controls', 'select'):
                self.keys['select'] = self.settings.getint('controls', 'select')
            if self.settings.has_option('controls', 'cancel'):
                self.keys['cancel'] = self.settings.getint('controls', 'cancel')
        
    def write(self):
        # write screen options
        if not self.settings.has_section('screen'):
            self.settings.add_section('screen')
        self.settings.set('screen', 'height', str(self.resolution[1]))
        self.settings.set('screen', 'width', str(self.resolution[0]))
        if self.fullscreen:
            self.settings.set('screen', 'fullscreen', 'true')
        else:
            self.settings.set('screen', 'fullscreen', 'false')
        if self.doublebuffer:
            self.settings.set('screen', 'doublebuffer', 'true')
        else:
            self.settings.set('screen', 'doublebuffer', 'false')
        if self.hardwareacceleration:
            self.settings.set('screen', 'hardwareacceleration', 'true')
        else:
            self.settings.set('screen', 'hardwareacceleration', 'false')
        
        # write controls
        if not self.settings.has_section('controls'):
            self.settings.add_section('controls')
        self.settings.set('controls', 'up', self.keys['up'])
        self.settings.set('controls', 'down', self.keys['down'])
        self.settings.set('controls', 'left', self.keys['left'])
        self.settings.set('controls', 'right', self.keys['right'])
        self.settings.set('controls', 'select', self.keys['select'])
        self.settings.set('controls', 'cancel', self.keys['cancel'])
        
        # write the file            
        file = open(self.settings_file, 'w')
        self.settings.write(file)
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
        