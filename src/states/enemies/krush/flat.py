from src.animation import Animation
from src.states.enemies.state import State

class FlatState(State):
    def __init__(self, enemy):
        animations = {
            'left': Animation(('enemies', 'krush'), ('flat_left_1', 'flat_left_2', 'flat_left_3'), 100),
            'right': Animation(('enemies', 'krush'), ('flat_right_1', 'flat_right_2', 'flat_right_3'), 100)
        }
        
        self.counter = 0
        self.flat_time = 5000
        
        State.__init__(self, enemy, animations, .1, 0)
    
    def process(self, tick_data):
        self.counter += tick_data['time_passed']
        
        if self.counter > self.flat_time:
            return 'walk'
        
        self.check_collisions()
        
        return 'flat'