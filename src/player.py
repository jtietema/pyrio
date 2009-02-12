
import sys

from pygame.locals import *

from movable_entity import MovableEntity
from game_entity import GameEntity

from states.player.walking import WalkingState
from states.player.standing import StandingState
from states.player.jumping import JumpingState
from states.player.falling import FallingState

class Player(MovableEntity):
    MAX_JUMPING_TIME = 600

    MIN_X_SPEED = .1
    MAX_X_SPEED = .35

    MIN_Y_SPEED = .15
    MAX_Y_SPEED = .5

    def __init__(self, position, map):
        MovableEntity.__init__(self, position, (56, 60), map)
        
        # Player starts in falling state
        self.falling = True

        self.states = {
            'walking' : WalkingState(self),
            'standing': StandingState(self),
            'jumping' : JumpingState(self),
            'falling' : FallingState(self)
        }
        self.currentState = self.states['falling']
    
    def update(self, tick_data):
        MovableEntity.update(self, tick_data)
        
    def render(self, screen):
        """Always renders the player in the center of the screen."""
        x_screen = screen.get_width() / 2 - self.rect.width / 2
        y_screen = screen.get_height() / 2 - self.rect.height / 2
        
        animation = self.get_animation()
        offset_x, offset_y = animation.get_image().get_offset()
        screen.blit(animation.get_image().get_surface(), (x_screen + offset_x, y_screen + offset_y))
    
    def hit(self, tick_data):
        """Called by an enemy when the player gets hit."""
        tick_data['killed'] = True
        
