
from game_entity import GameEntity
from movable_entity import MovableEntity

class Enemy(MovableEntity):
    def __init__(self, position, size, map):
        MovableEntity.__init__(self, position, size, map)
        
        self.player = None
    
    def update(self, tick_data):
        MovableEntity.update(self, tick_data)
    
    def render(self, screen, map_offsets):
        MovableEntity.render(self, screen, map_offsets)

    def set_player(self, player):
        """Adds a reference to the player object to the enemy after the world has been
        initialized."""
        self.player = player
    
    def is_hit_by_player(self):
        """Detects if the enemy is hit by the player."""
        p_rect = self.player.get_previous_rect()
        return self.collides_with_player() and p_rect.y < self.player.get_rect().y
    
    def collides_with_player(self):
        """Detects if this enemy collides with the player."""
        return self.collide(self.player.get_rect())
    
    def hit_player(self, tick_data):
        """Hits the player entity."""
        self.player.hit(tick_data)
    
    def bounce_player(self, tick_data):
        """Makes sure the player bounces upward, using this entity's top y to set the
        origin of the player's jump."""
        self.player.bounce(tick_data, self.rect.top)