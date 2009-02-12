
from src.states.state import State
from src.animation import Animation
from src.game_entity import GameEntity

from pygame.locals import *

class AbstractJumpingState(State):
    def __init__(self, player):
        animations = {
            'left' : Animation('player', ('jump_left', )),
            'right': Animation('player', ('jump_right',))
        }
        State.__init__(self, player, animations, .3, .5)
        
        self.name = None

        self.jumping_time = 0

    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        actions = tick_data['actions']

        # stop jumping if the jump key is released
        if not self.should_continue_jumping(tick_data):
            return 'falling'

        # process jump
        x_delta = time_passed * self.x_speed * actions.x
        if actions.x < 0:
            self.entity.direction = GameEntity.DIRECTION_LEFT
        elif actions.x > 0:
            self.entity.direction = GameEntity.DIRECTION_RIGHT
        else:
            x_delta = 0

        y_delta = time_passed * self.y_speed * -1
        self.jumping_time += time_passed

        self.entity.move(x_delta, y_delta)
        
        return self.name

    def reset(self):
        self.jumping_time = 0