
import sys

from asset_manager import AssetManager

class Menu():
    MAX_INDEX = 1
    
    def __init__(self):
        self.index = 0
        self.flower = AssetManager.get_image(('menu','items'), 'flower')
        self.menu_items = [
            AssetManager.get_image('menu','start'),
            AssetManager.get_image('menu','quit')
        ]
        self.screen_size = None

    def update(self, tick_data):
        actions = tick_data['actions']
        self.screen_size = tick_data['screen_size']

        if actions.select:
            self.select(self.index, tick_data)

        if actions.y > 0 and self.index is not 0:
            self.index -= 1
        if actions.y < 0 and self.index is not Menu.MAX_INDEX:
            self.index += 1

    def select(self, index, tick_data):
        if index is 0:
            tick_data['pause'] = False
        elif index is 1:
            print 'Bye...'
            sys.exit()

    def render(self, screen):
        width, height = self.screen_size
        width /= 2

        height /= 2
        height = (Menu.MAX_INDEX + 1) / 2 * 150

        for index in range(Menu.MAX_INDEX+1):
            image = self.menu_items[index].get_surface()
            if index is self.index:
                #selected
                screen.blit(self.flower.get_surface(), (width - 260, height))
            screen.blit(image, (width - (image.get_size()[0]/2), height))
            height += 150