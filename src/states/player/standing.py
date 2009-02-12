
from src.states.state import State
from src.animation import Animation

from pygame.locals import *

class StandingState(State):
    def __init__(self, player):
        animations = {
                'left': Animation('player', ('stand_left',)),
                'right': Animation('player', ('stand_right',))
        }
        State.__init__(self, player, animations, .3, .5)

    def process(self, tick_data):
        actions = tick_data['actions']
        if actions.x is not 0:
            return 'walking'
        elif actions.jump:
            return 'jumping'
        else:
            return 'standing'
        
        