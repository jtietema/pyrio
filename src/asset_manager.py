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
from ConfigParser import RawConfigParser
from image import Image

class AssetManager:
    loaded_assets = {
        "images": {}
    }
    
    IMAGE_DEFAULT_WIDTH = 64
    IMAGE_DEFAULT_HEIGHT = 64
    
    @classmethod
    def get_image(cls, group, name):
        images = cls.loaded_assets['images']
        
        if not isinstance(group, list) and not isinstance(group, tuple):
            group = [group]
        
        group_folder = os.path.join('assets', 'images', *group)
        
        if group_folder not in images:
            images[group_folder] = {}
        if name not in images[group_folder]:
            # We load the whole group at once for performance reasons. Moreover, images
            # in a group are closely related and will probably be loaded anyway.
            config_file = os.path.join(group_folder, 'pkg.cfg')
            
            config = RawConfigParser()
            config.read(config_file)
            
            sections = config.sections()
            
            if name not in sections:
                raise Exception("Unknown image specified: %s => %s" % (group, name))
                return False
            
            for section in sections:
                if section == '__default__': continue
                
                file_path = os.path.join(group_folder, config.get(section, 'file'))
                image = pygame.image.load(file_path).convert_alpha()
                
                # Scale image?
                if config.has_option(section, 'width'):
                    width = config.getint(section, 'width')
                elif config.has_option('__default__', 'width'):
                    width = config.getint('__default__', 'width')
                else:
                    width = cls.IMAGE_DEFAULT_WIDTH
                
                if config.has_option(section, 'height'):
                    height = config.getint(section, 'height')
                elif config.has_option('__default__', 'height'):
                    height = config.getint('__default__', 'height')
                else:
                    height = cls.IMAGE_DEFAULT_HEIGHT
                
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
                
                images[group_folder][section] = Image(image, (offset_x, offset_y))
        
        return images[group_folder][name]
    
    @classmethod
    def get_sound(cls, group, name):        
        return pygame.mixer.Sound(os.path.join('assets', 'sounds', 'player', 'dead.ogg'))
