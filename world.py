
class World():
    def __init__(self):
        self.player = Player()
        self.map = Map(player)
        
    def update(self, state):
        self.player.update(state)
        self.map.update(state)
        
    def render(self, screen):
        screen.fill((164,252, 255))
        self.map.render(screen)
        self.player.render(screen)
        