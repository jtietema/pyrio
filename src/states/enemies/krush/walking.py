
from src.animation import Animation
from src.states.enemies.moving import MovingState

import src.assets as assets

class WalkingState(MovingState):
    def __init__(self, enemy):
        animations = {
            'left': Animation(assets.images.enemies.krush, ('walk_left_1', 'walk_left_2', 'walk_left_3'), 100),
            'right': Animation(assets.images.enemies.krush, ('walk_right_1', 'walk_right_2', 'walk_right_3'), 100)
        }
        
        MovingState.__init__(self, enemy, animations, .3, 0)
    
    def process(self, tick_data):
        MovingState.process(self, tick_data)
        
        if self.entity.collides_with_player():
            if self.entity.is_hit_by_player():
                self.entity.bounce_player(tick_data)
                return 'flat'
            
            self.entity.hit_player(tick_data)
        
        return 'walk'