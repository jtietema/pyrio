
from pygame.locals import *
import pygame

from movable_entity import MovableEntity

from states.player.walking import WalkingState
from states.player.standing import StandingState
from states.player.jumping import JumpingState
from states.player.falling import FallingState
from states.player.bouncing import BouncingState

class Player(MovableEntity):
    def __init__(self, position, map):
        MovableEntity.__init__(self, position, (56, 60), map)

        self.states = {
            'walking' : WalkingState(self),
            'standing': StandingState(self),
            'jumping' : JumpingState(self),
            'falling' : FallingState(self),
            'bouncing': BouncingState(self)
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
        self.render_debug(screen)

    def render_debug(self, screen):
        if self.debug:
            x_screen = screen.get_width() / 2 - self.rect.width / 2
            y_screen = screen.get_height() / 2 - self.rect.height / 2
            pygame.draw.rect(screen, (0,255,0), (x_screen, y_screen, self.rect.w, self.rect.h), 1)
    
    def hit(self, tick_data):
        """Called by an enemy when the player gets hit."""
        tick_data['killed'] = True
    
    def bounce(self, tick_data, bottom):
        self.rect.bottom = bottom
        self.currentState = self.states['bouncing']
        self.currentState.reset()
        self.get_animation().reset()
        
        self.update(tick_data)
