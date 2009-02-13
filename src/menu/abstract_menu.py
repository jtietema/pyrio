# -*- coding: utf-8 -*-

from src.asset_manager import AssetManager

class AbstractMenu():
    def __init__(self):
        self.index = 0
        self.flower = AssetManager.get_image(('menu','items'), 'flower')
        self.screen_size = None
        self.timeout = 0
        self.menu()
        self.submenu = None
    
    def update(self, tick_data):
        actions = tick_data['actions']
        self.screen_size = tick_data['screen_size']
        
        if actions.select:
            self.select(self.index, tick_data)
        
        if actions.cancel:
            if self.submenu is None:
                print 'escape menu'
                tick_data['pause'] = False
            else:
                self.submenu = None
        
        if actions.y > 0 and self.index is not 0 and self.timeout is 0:
            self.index -= 1
            self.timeout = 300
        if actions.y < 0 and self.index is not self.max_index and self.timeout is 0:
            self.index += 1
            self.timeout = 300
        
        if self.timeout > 0:
            self.timeout -= tick_data['time_passed']
        else:
            self.timeout = 0
    
    def render(self, screen):
        width, height = self.screen_size
        width /= 2
        
        height /= 2
        height = (self.max_index + 1) / 2 * 150
        
        for index in range(self.max_index + 1):
            image = self.menu_items[index].get_surface()
            if index is self.index:
                #selected
                screen.blit(self.flower.get_surface(), (width - 260, height))
            screen.blit(image, (width - (image.get_size()[0]/2), height))
            height += 150