
from game_entity import GameEntity
from movable_entity import MovableEntity

class Enemy(MovableEntity):
    def __init__(self, position, map):
        MovableEntity.__init__(self, position, (64, 64), map)
        
        self.player = None
    
    def update(self, tick_data):
        MovableEntity.update(self, tick_data)
    
    def render(self, screen, map_offsets):
        MovableEntity.render(self, screen, map_offsets)

    def set_player(self, player):
        """Adds a reference to the player object to the enemy after the world has been
        initialized."""
        self.player = player
    
    def collides_with_player(self):
        """Detects if this enemy collides with the player."""
        return self.collide(self.player.get_rect())
    
    def hit_player(self, tick_data):
        """Hits the player entity."""
        self.player.hit(tick_data)