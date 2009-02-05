
from player import Player
from map import Map

class World():
    def __init__(self):
        self.player = Player()
        self.map = Map('test', self.player)
        
    def update(self, tick_data):
        self.player.update(tick_data)
        self.map.update(tick_data)
        
    def render(self, screen):
        screen.fill((164,252, 255))
        self.map.render(screen)
        self.player.render(screen)
        