
from src.states.state import State as AbstractState

class State(AbstractState):
    def __init__(*args):
        AbstractState.__init__(*args)
    
    def update(self, tick_data):
        target_state = AbstractState.update(self, tick_data)
        
        self.check_collisions(tick_data)
        
        return target_state
    
    def check_collisions(self, tick_data):
        """Check for collisions with the player. Hit the player if any collisions."""
        if self.entity.collides_with_player():
            self.entity.hit_player(tick_data)