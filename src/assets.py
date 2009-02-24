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
import os
from glob import glob
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
    # When set to true, loads all the assets in the folder when it is initialized, by
    # calling load_assets(). This method is not implemented by this abstract base class,
    # so it must be written on the implementation classes.
    PRELOAD_ASSETS = True
    
    # Initializes all subfolders of this folder as soon as this one is initialized.
    COLLECT_FOLDERS_RECURSIVELY = False
    
    def __init__(self, name, parent=None):
        """Creates a new asset folder instance. Throws an exception if the directory
        does not exist."""
        self._name = name
        self._parent = parent
        
        if not os.path.isdir(self.get_path()):
            raise AssetFolderException("Unknown asset or folder '%s'." % (name,))
        
        if self.__class__.PRELOAD_ASSETS:
            self.load_assets()
        
        if self.__class__.COLLECT_FOLDERS_RECURSIVELY:
            self.load_nested_folders()
    
    def __str__(self):
        """String representation of this folder, which equals its relative path."""
        return self.get_path()
    
    def __getattr__(self, name):
        """Magically called when an attribute doesn't exist. This currently assumes
        the requested attribute is a folder, since all current implementations preload
        all assets when a folder is initialized."""
        try:
            self.__dict__[name] = self.load_asset(name)
        except:
            self.__dict__[name] = self.load_nested_folder(name)
        
        return self.__dict__[name]
    
    def load_asset(self, name):
        raise AssetFolderException("Unknown asset '%s'" % (name,))
    
    def get_path(self):
        """Returns the folder as a relative path from the main folder."""
        if self._parent is None:
            return self._name
    
        return os.path.join(self._parent.get_path(), self._name)
    
    def get(self, name):
        """Returns a single asset based on its name. This is restricted to the scope
        of this folder, meaning it will not look for the file recursively."""
        if not self.__dict__[arg]:
            raise AssetFolderException("No attribute '%s'" % (arg,))
        if isinstance(self.__dict__[arg], AssetFolder):
            raise AssetFolderException("'%s' is a folder, not an asset" % (arg,))
        
        return self.__dict__[arg]
    
    def get_multiple(self, *args):
        """Returns multiple assets in a list based on the arguments passed in. Throws an
        AssetFolderException if any of the arguments is a folder."""
        result = {}
        for arg in args:
            result[arg] = self.get(arg)
            
        return result
    
    def load_nested_folder(self, name):
        """Creates an AssetFolder object for the specified nested folder, and sets it
        on this object as an attribute."""
        folder = self.__class__(name, self)
        self.__dict__[name] = folder
        return folder
    
    def load_nested_folders(self):
        """Finds all the nested folders recursively and initializes them."""
        for item in os.listdir(self.get_path()):
            if os.path.isdir(os.path.join(self.get_path(), item)):
                self.load_nested_folder(item)


class ImageFolder(AssetFolder):
    def load_assets(self):
        """Tries to load the assets in this folder. Only loads assets defined in a
        pkg.cfg file in this folder, which should adhere to the syntax known by the
        ConfigParser module."""
        config_file = os.path.join(self.get_path(), 'pkg.cfg')
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
        """Parses one file (i.e. one section) in the config file. This also takes care
        of parsing options in the config file (including optional defaults for settings).
        This method returns an Image object, containing the surface as well as some
        additional information like offsets to fix the bounding box."""
        file_path = os.path.join(self.get_path(), config.get(section, 'file'))
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
        elif config.has_option('__default__', 'offset_x'):
            offset_x = config.getint('__default__', 'offset_x')

        offset_y = 0
        if config.has_option(section, 'offset_y'):
            offset_y = config.getint(section, 'offset_y')
        elif config.has_option('__default__', 'offset_y'):
            offset_y = config.getint('__default__', 'offset_y')
        
        self.__dict__[section] = Image(image, (offset_x, offset_y))


class SoundFolder(AssetFolder):
    """Represents a folder containing sound files. Since sound files will not be altered
    using settings, we are not using package configuration files. Instead, we assume all
    sound files are ogg files."""
    
    COLLECT_FOLDERS_RECURSIVELY = True
    
    def load_assets(self):
        """Loads all the sounds in this folder. Assumes all the sounds are ogg files,
        and thus have a .ogg extension."""
        for sound_file in glob(self.get_path() + '/*.ogg'):
            filename_base = os.path.splitext(os.path.basename(sound_file))[0]
            self.__dict__[filename_base] = pygame.mixer.Sound(sound_file)
    

# Asset instances
images = ImageFolder(os.path.join(ASSETS_ROOT, 'images'))
sounds = SoundFolder(os.path.join(ASSETS_ROOT, 'sounds'))