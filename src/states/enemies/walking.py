
from src.game_entity import GameEntity
from src.states.enemies.state import State

class WalkingState(State):
    def __init__(*args):
        State.__init__(*args)
    
    def process(self, tick_data):
        x_delta = tick_data['time_passed'] * self.x_speed
        
        heading_left = self.entity.direction is GameEntity.DIRECTION_LEFT
        
        if heading_left:
            x_delta *= -1
        
        # Flip the direction if the requested movement could not be performed.
        if not self.entity.move(x_delta, 0):
            self.entity.direction = GameEntity.DIRECTION_RIGHT if heading_left else GameEntity.DIRECTION_LEFT
        
        return 'walk'