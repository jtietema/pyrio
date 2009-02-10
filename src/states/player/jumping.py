
from src.states.state import State
from src.animation import Animation
from src.game_entity import GameEntity

from pygame.locals import *

class JumpingState(State):
    MAX_JUMPING_TIME = 600

    MIN_X_SPEED = .1
    MAX_X_SPEED = .35

    MIN_Y_SPEED = .15
    MAX_Y_SPEED = .5
    
    def __init__(self, player):
        animations = {
            'left' : Animation('player', ('jump_left', )),
            'right': Animation('player', ('jump_right',))
        }
        State.__init__(self, player, animations, .1, .15)

        self.jumping_time = 0

    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        pressed_keys = tick_data['pressed_keys']

        # stop jumping if the jump key is released
        if not pressed_keys[K_UP] or self.jumping_time > JumpingState.MAX_JUMPING_TIME:
            return 'falling'

        # process jump
        x_delta = time_passed * self.x_speed
        if pressed_keys[K_LEFT]:
            x_delta *= -1
            self.entity.direction = GameEntity.DIRECTION_LEFT
            if self.x_speed < JumpingState.MAX_X_SPEED:
                self.x_speed *= 1.007
        elif pressed_keys[K_RIGHT]:
            self.entity.direction = GameEntity.DIRECTION_RIGHT
            if self.x_speed < JumpingState.MAX_X_SPEED:
                self.x_speed *= 1.007
        else:
            x_delta = 0
            self.x_speed = JumpingState.MIN_X_SPEED

        if self.y_speed > self.MIN_Y_SPEED:
            self.y_speed /= 1.007
        y_delta = time_passed * self.y_speed * -1
        self.jumping_time += time_passed

        self.move(x_delta, y_delta)
        return 'jumping'

    def reset(self):
        self.y_speed = JumpingState.MAX_Y_SPEED
        self.jumping_time = 0