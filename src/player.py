"""
This file is part of Pyrio.

Pyrio is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pyrio is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pyrio.  If not, see <http://www.gnu.org/licenses/>.
"""
from pygame.locals import *
from game_locals import *
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
        MovableEntity.__init__(self, position, (48, 60), map)

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
            pygame.event.post(pygame.event.Event(PLAYER_DEATH))
            
            AssetManager.get_sound('test', 'test').play()
    
    def bounce(self, tick_data, bottom):
        self.rect.bottom = bottom
        
        self.switch_state('bouncing')
        
        self.update(tick_data)
