
from src.animation import Animation
from src.states.enemies.walking import WalkingState as AbstractWalkingState

class WalkingState(AbstractWalkingState):
    def __init__(self, enemy):
        animations = {
            'left': Animation(('enemies', 'krush'), ('walk_left_1', 'walk_left_2', 'walk_left_3'), 100),
            'right': Animation(('enemies', 'krush'), ('walk_right_1', 'walk_right_2', 'walk_right_3'), 100)
        }
        
        AbstractWalkingState.__init__(self, enemy, animations, .3, 0)