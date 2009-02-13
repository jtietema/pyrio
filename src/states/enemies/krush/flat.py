from src.animation import Animation
from src.states.enemies.moving import MovingState

class FlatState(MovingState):
    def __init__(self, enemy):
        animations = {
            'left': Animation(('enemies', 'krush'), ('flat_left_1', 'flat_left_2', 'flat_left_3'), 100),
            'right': Animation(('enemies', 'krush'), ('flat_right_1', 'flat_right_2', 'flat_right_3'), 100)
        }
        
        self.counter = 0
        self.max_flat_time = 5000
        
        MovingState.__init__(self, enemy, animations, .1, 0)
    
    def process(self, tick_data):        
        MovingState.process(self, tick_data)
        
        self.counter += tick_data['time_passed']
        
        if self.counter > self.max_flat_time:
            return 'walk'
        
        if self.entity.collides_with_player():
            if self.entity.is_hit_by_player():
                self.entity.bounce_player(tick_data)
                self.counter = 0
        
        return 'flat'
    
    def enter(self):
        MovingState.enter(self)
        
        self.counter = 0
        self.entity.rect.size = (60, 44)
        self.entity.rect.move_ip(0, 8)
    
    def exit(self):
        MovingState.exit(self)
        
        self.entity.rect.size = self.entity.default_size
        self.entity.rect.move_ip(0, -8)