
from ..state import State
from ...animation import Animation

from pygame.locals import *

class StandingState(State):
    def __init__(self, player):
        animations = {
                'left': Animation('player', ('stand_left',)),
                'right': Animation('player', ('stand_right',))
        }
        State.__init__(self, player, animations, .1, .15)

    def process(self, tick_data):
        pressed_keys = tick_data['pressed_keys']
        if pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]:
            return 'walking'
        elif pressed_keys[K_UP]:
            return 'jumping'
        else:
            return 'standing'
        
        