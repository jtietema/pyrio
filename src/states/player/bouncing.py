from src.states.player.abstract_jumping import AbstractJumpingState

class BouncingState(AbstractJumpingState):
    MAX_JUMPING_TIME = 200
    
    def __init__(self, player):
        AbstractJumpingState.__init__(self, player)
        
        self.name = 'bouncing'
    
    def should_continue_jumping(self, tick_data):
        return self.jumping_time <= BouncingState.MAX_JUMPING_TIME