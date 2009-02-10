
from src.states.state import State
from src.animation import Animation
from src.game_entity import GameEntity

from pygame.locals import *

class WalkingState(State):
    MIN_X_SPEED = .1
    MAX_X_SPEED = .35

    def __init__(self, player):
        animations = {
            'left': Animation('player', ('walk_left_1', 'walk_left_2'), 200),
            'right': Animation('player', ('walk_right_1', 'walk_right_2'), 200)
        }
        State.__init__(self, player, animations, .1, .15)

    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        pressed_keys = tick_data['pressed_keys']
        x_delta = time_passed * self.x_speed

        next_state = 'walking'
        if pressed_keys[K_LEFT]:
            x_delta *= -1
            self.entity.direction = GameEntity.DIRECTION_LEFT
            if self.x_speed < WalkingState.MAX_X_SPEED:
                self.x_speed *= 1.007
        elif pressed_keys[K_RIGHT]:
            self.entity.direction = GameEntity.DIRECTION_RIGHT
            if self.x_speed < WalkingState.MAX_X_SPEED:
                self.x_speed *= 1.007
        else:
            x_delta = 0
            next_state = 'standing'
            self.x_speed = WalkingState.MIN_X_SPEED

        if pressed_keys[K_UP]:
            next_state = 'jumping'

        self.move(x_delta, 0)

        return next_state
