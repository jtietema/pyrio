
from asset_manager import AssetManager

class Hud():
    def __init__(self, game):
        self.game = game
        self.lives = AssetManager.get_image('game','lives')

    def update(self, tick_data):
        pass

    def render(self, screen):
        for live in range(self.game.get_lives()):
            screen.blit(self.lives.get_surface(), (20 * (live+1), 10))