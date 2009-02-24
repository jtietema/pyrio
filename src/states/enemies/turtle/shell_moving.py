
from src.animation import Animation
from src.states.enemies.moving import MovingState

import src.assets as assets

class ShellMovingState(MovingState):
    def __init__(self, enemy):
        animations = {
            'moving': Animation(assets.images.enemies.turtle, ('shell_move_1', 'shell_move_2', 'shell_move_3'), 100)
        }
        
        MovingState.__init__(self, enemy, animations, .5)

    def get_animation(self):
        return self.animations['moving']
    
    def process(self, tick_data):
        MovingState.process(self, tick_data)
        
        if self.entity.collides_with_player():
            self.entity.hit_player(tick_data)
        
        return 'shell_moving'
            
    def enter(self):
        MovingState.enter(self)
        
        self.entity.rect.size = (42, 36)
        self.entity.rect.move_ip(0, 28)

    def exit(self):
        MovingState.exit(self)
        
        self.entity.rect.size = self.entity.default_size
        self.entity.rect.move_ip(0, -28)