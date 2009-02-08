
import pygame
import os

class AssetManager:
    loaded_assets = {
        "images": {}
    }
    
    @classmethod
    def get_image(cls, group, name):
        images = cls.loaded_assets['images']
        
        if not images.has_key(group):
            images[group] = {}
        if not images[group].has_key(name):
            file_path = os.path.join('assets', 'images', group, name)
            images[group][name] = pygame.image.load(file_path).convert()
        
        return images[group][name]