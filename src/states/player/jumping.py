
from src.states.player.abstract_jumping import AbstractJumpingState

class JumpingState(AbstractJumpingState):
    MAX_JUMPING_TIME = 600
    
    def __init__(self, player):
        AbstractJumpingState.__init__(self, player)
        
        self.name = 'jumping'
    
    def should_continue_jumping(self, tick_data):
        """Determines if the player should continue jumping."""
        return tick_data['actions'].jump and self.jumping_time <= JumpingState.MAX_JUMPING_TIME