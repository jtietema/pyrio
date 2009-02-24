# -*- coding: utf-8 -*-

from src.states.state import State
from src.animation import Animation
from src.game_entity import GameEntity

from pygame.locals import *

import src.assets as assets

class FallingState(State):
    
    def __init__(self, player):
        animations = {
            'left' : Animation(assets.images.player, ('fall_left', )),
            'right': Animation(assets.images.player, ('fall_right',))
        }
        State.__init__(self, player, animations, .3, .5)

    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        actions = tick_data['actions']

        y_delta = time_passed * self.y_speed
        
        # check if still falling
        if not self.entity.check_falling(time_passed * self.y_speed):
            # check if we really can't fall another pixel
            y_delta = int(time_passed * self.y_speed)
            while y_delta > 0:
                y_delta -= 1
                if self.entity.check_falling(y_delta):
                    break
            
            if y_delta is 0:
                if actions.x is not 0:
                    return 'walking'
                else:
                    return 'standing'

        # continue falling
        x_delta = self.x_speed * time_passed * actions.x
        if actions.x < 0:
            self.entity.direction = GameEntity.DIRECTION_LEFT
        elif actions.x > 0:
            self.entity.direction = GameEntity.DIRECTION_RIGHT
        else:
            x_delta = 0

        self.entity.move(x_delta, y_delta)
        return 'falling'
