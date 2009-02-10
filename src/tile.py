from game_entity import GameEntity
from asset_manager import AssetManager

class Tile(GameEntity):
    def __init__(self, name, (x, y)):
        self.image = AssetManager.get_image('map', name)
        
        GameEntity.__init__(self, (x, y), self.image.get_size())
    
    def render(self, screen, offsets):
        GameEntity.render(self, screen, self.image, offsets)