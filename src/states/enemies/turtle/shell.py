from src.animation import Animation
from src.game_entity import GameEntity
from src.states.state import State

class ShellState(State):
    def __init__(self, enemy):
        animations = {
            'shell': Animation(('enemies', 'turtle'), ('shell_front',))
        }
        
        State.__init__(self, enemy, animations)
    
    def get_animation(self, direction):
        return self.animations['shell']
    
    def process(self, tick_data):
        if self.entity.collides_with_player():
            if self.entity.is_hit_by_player():
                self.entity.bounce_player(tick_data)
            
            if self.entity.get_rect().centerx < self.entity.player.get_rect().centerx:
                self.entity.direction = GameEntity.DIRECTION_LEFT
            else:
                self.entity.direction = GameEntity.DIRECTION_RIGHT
            
            return 'shell_moving'
            
        return 'shell'
    
    def enter(self):
        self.entity.rect.size = (42, 36)
        self.entity.rect.move_ip(0, 28)
    
    def exit(self):
        self.entity.rect.size = self.entity.default_size
        self.entity.rect.move_ip(0, -28)