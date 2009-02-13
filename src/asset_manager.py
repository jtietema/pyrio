# -*- coding: utf-8 -*-

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

                offset_y = 0
                if config.has_option(section, 'offset_y'):
                    offset_y = config.getint(section, 'offset_y')
                elif config.has_option('__default__', 'offset_y'):
                    offset_y = config.getint('__default__', 'offset_y')
                
                images[group_folder][section] = Image(image, (offset_x, offset_y))
        
        return images[group_folder][name]
        