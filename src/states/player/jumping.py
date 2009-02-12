
from src.states.state import State
from src.animation import Animation
from src.game_entity import GameEntity

from pygame.locals import *

class JumpingState(State):
    MAX_JUMPING_TIME = 600

    def __init__(self, player):
        animations = {
            'left' : Animation('player', ('jump_left', )),
            'right': Animation('player', ('jump_right',))
        }
        State.__init__(self, player, animations, .3, .5)

        self.jumping_time = 0

    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        actions = tick_data['actions']

        # stop jumping if the jump key is released
        if not actions.jump or self.jumping_time > JumpingState.MAX_JUMPING_TIME:
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

        self.move(x_delta, y_delta)
        return 'jumping'

    def reset(self):
        self.jumping_time = 0