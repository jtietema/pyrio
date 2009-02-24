# -*- coding: utf-8 -*-

import pygame
import os
from ConfigParser import RawConfigParser
from image import Image


# Module constants
ASSETS_ROOT = 'assets'
DEFAULTS_CONFIG_SECTION = '__default__'

DEFAULT_WIDTH = 64
DEFAULT_HEIGHT = 64


class AssetFolderException(Exception):
    pass


class AssetFolder:    
    def __init__(self, name, parent):
        """Creates a new asset folder instance. Throws an exception if the directory
        does not exist."""
        self._name = name
        self._parent = parent
        
        if not os.path.isdir(str(self)):
            raise AssetFolderException("Unknown image, or requested folder does not exist.")
    
    def __str__(self):
        """Returns the folder as a relative path from the manager's root folder."""
        if self._parent is None:
            return self._name
        
        return os.path.join(str(self._parent), self._name)
    
    def __getattr__(self, name):
        """Magically called when an attribute doesn't exist."""
        folder = self.__class__(name, self)
        self.__dict__[name] = folder
        return folder


class ImageFolder(AssetFolder):    
    def __init__(self, *args):
        AssetFolder.__init__(self, *args)
        
        self.load_assets()
    
    def load_assets(self):
        """Tries to load the assets in this folder. Only loads assets defined in a
        pkg.cfg file in this folder, which should adhere to the syntax known by the
        ConfigParser module."""
        config_file = os.path.join(str(self), 'pkg.cfg')
        if os.path.isfile(config_file):
            self.parse_config(config_file)
    
    def parse_config(self, config_file):
        """Parses the config file passed in and loads the images."""
        config = RawConfigParser()
        config.read(config_file)
        
        sections = config.sections()
        
        for section in sections:
            if section == DEFAULTS_CONFIG_SECTION: continue
            
            self.parse_file(config, section)
    
    def parse_file(self, config, section):
        """Parses one file (i.e. one section) in the config file."""
        file_path = os.path.join(str(self), config.get(section, 'file'))
        image = pygame.image.load(file_path).convert_alpha()
        
        # Scale image?
        if config.has_option(section, 'width'):
            width = config.getint(section, 'width')
        elif config.has_option('__default__', 'width'):
            width = config.getint('__default__', 'width')
        else:
            width = DEFAULT_WIDTH
        
        if config.has_option(section, 'height'):
            height = config.getint(section, 'height')
        elif config.has_option('__default__', 'height'):
            height = config.getint('__default__', 'height')
        else:
            height = DEFAULT_HEIGHT
        
        if image.get_size() != (width, height):
            image = pygame.transform.smoothscale(image, (width, height))
        
        # Flip image?
        flip_x = config.has_option(section, 'flip_x') and config.getboolean(section, 'flip_x')
        flip_y = config.has_option(section, 'flip_y') and config.getboolean(section, 'flip_y')
        if flip_x or flip_y:
            image = pygame.transform.flip(image, flip_x, flip_y)

        # read if offset is present
        offset_x = 0
        if config.has_option(section, 'offset_x'):
            offset_x = config.getint(section, 'offset_x')

        offset_y = 0
        if config.has_option(section, 'offset_y'):
            offset_y = config.getint(section, 'offset_y')
        elif config.has_option('__default__', 'offset_y'):
            offset_y = config.getint('__default__', 'offset_y')
        
        self.__dict__[section] = Image(image, (offset_x, offset_y))

# Create an images assets folder instance
images = ImageFolder(os.path.join(ASSETS_ROOT, 'images'), None)