
from ..state import State
from ...animation import Animation
from ...game_entity import GameEntity

from pygame.locals import *

class FallingState(State):
    MIN_X_SPEED = .1
    MAX_X_SPEED = .35

    MIN_Y_SPEED = .15
    MAX_Y_SPEED = .5
    
    def __init__(self, player):
        animations = {
            'left' : Animation('player', ('fall_left', )),
            'right': Animation('player', ('fall_right',))
        }
        State.__init__(self, player, animations, .1, .15)

    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        pressed_keys = tick_data['pressed_keys']

        # check if still falling
        if not self.entity.check_falling(time_passed * self.y_speed):
            if pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]:
                return 'walking'
            else:
                return 'standing'

        # continue falling
        x_delta = self.x_speed * time_passed
        if pressed_keys[K_LEFT]:
            x_delta *= -1
            self.entity.direction = GameEntity.DIRECTION_LEFT
            if self.x_speed < FallingState.MAX_X_SPEED:
                self.x_speed *= 1.007
        elif pressed_keys[K_RIGHT]:
            self.entity.direction = GameEntity.DIRECTION_RIGHT
            if self.x_speed < FallingState.MAX_X_SPEED:
                self.x_speed *= 1.007
        else:
            x_delta = 0
            self.x_speed = FallingState.MIN_X_SPEED
        y_delta = time_passed * self.y_speed
        if self.y_speed < FallingState.MAX_Y_SPEED:
            self.y_speed *= 1.1

        self.move(x_delta, y_delta)
        return 'falling'

    def reset(self):
        self.y_speed = FallingState.MIN_Y_SPEED
