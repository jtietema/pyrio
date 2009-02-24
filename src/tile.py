from game_entity import GameEntity
import assets

class Tile(GameEntity):
    def __init__(self, name, (x, y)):
        self.image = assets.images.map.__dict__[name]
        
        GameEntity.__init__(self, (x, y), self.image.get_size())
    
    def render(self, screen, offsets):
        GameEntity.render(self, screen, self.image, offsets)