
from pygame.locals import *
import pygame

from movable_entity import MovableEntity
from asset_manager import AssetManager

from states.player.walking import WalkingState
from states.player.standing import StandingState
from states.player.jumping import JumpingState
from states.player.falling import FallingState
from states.player.bouncing import BouncingState
from states.player.dead import DeadState

class Player(MovableEntity):
    def __init__(self, position, map):
        MovableEntity.__init__(self, position, (56, 60), map)

        self.states = {
            'walking' : WalkingState(self),
            'standing': StandingState(self),
            'jumping' : JumpingState(self),
            'falling' : FallingState(self),
            'bouncing': BouncingState(self),
            'dead':     DeadState(self)
        }
        self.currentState = self.states['falling']
        
        self.dead = False
    
    def update(self, tick_data):
        MovableEntity.update(self, tick_data)
        
    def render(self, screen):
        """Always renders the player in the center of the screen."""
        x_screen = screen.get_width() / 2 - self.rect.width / 2
        y_screen = screen.get_height() / 2 - self.rect.height / 2
        
        image = self.currentState.get_image()
        offset_x, offset_y = image.get_offset()
        screen.blit(image.get_surface(), (x_screen + offset_x, y_screen + offset_y))
        self.render_debug(screen)

    def render_debug(self, screen):
        if self.debug:
            x_screen = screen.get_width() / 2 - self.rect.width / 2
            y_screen = screen.get_height() / 2 - self.rect.height / 2
            pygame.draw.rect(screen, (0,255,0), (x_screen, y_screen, self.rect.w, self.rect.h), 1)
    
    def hit(self, tick_data):
        """Called by an enemy when the player gets hit."""
        if not self.dead:
            self.dead = True
            image = self.currentState.get_image()
            self.switch_state('dead')
            self.currentState.set_source_image(image)
            tick_data['dead'] = True
            
            AssetManager.get_sound('test', 'test').play()
    
    def bounce(self, tick_data, bottom):
        self.rect.bottom = bottom
        
        self.switch_state('bouncing')
        
        self.update(tick_data)
