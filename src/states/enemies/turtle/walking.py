
from src.animation import Animation
from src.states.enemies.walking import WalkingState as AbstractWalkingState

class WalkingState(AbstractWalkingState):
    def __init__(self, enemy):
        animations = {
            'left': Animation(('enemies', 'turtle'), ('walk_left_1', 'walk_left_2', 'walk_left_3'), 200),
            'right': Animation(('enemies', 'turtle'), ('walk_right_1', 'walk_right_2', 'walk_right_3'), 200)
        }
        
        AbstractWalkingState.__init__(self, enemy, animations, .15, 0)