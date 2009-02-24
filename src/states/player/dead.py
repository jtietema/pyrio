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
import pygame

from src.game_locals import *

from src.states.state import State
from src.image import Image

class DeadState(State):
    # Time in milliseconds it takes to spin 360 degrees.
    ROTATION_TIME = 750
    
    # Time before the player starts spinning.
    STILL_TIME = 500
    
    # The amount of time the player animates. Aggregate this with STILL_TIME
    # to get the full time the player stays in dead state.
    ANIMATION_TIME = 4000
    
    # The maximum scale value the dead animation should reach.
    MIN_SCALE_VALUE = 0.
       
    def __init__(self, player):
        self.entity = player
        
        self.image = None
        
        # Counter to store the time the player has been dead.
        self.counter = 0
        
        self.angle = 0.
        self.scale = 1.
        
        self.scale_delta = 1 - DeadState.MIN_SCALE_VALUE
        
        self.still = True
    
    def get_animation(self):
        """Return None, since we are not working with animations in this state."""
        return None
    
    def set_source_image(self, image):
        """Sets the image to use as a source. Since the player is frozen upon dying,
        we want to keep displaying the same image as the one that was active when the
        player died."""
        self.image = image
    
    def process(self, tick_data):
        self.counter += tick_data['time_passed']
        
        corrected_counter_value = self.counter - DeadState.STILL_TIME
        
        if corrected_counter_value > DeadState.ANIMATION_TIME:
            # Death animation is done, now is the time to restart the map.
            pygame.event.post(pygame.event.Event(DEATH_ANIMATION_DONE))
        elif corrected_counter_value >= 0:
            # We are past the still phase of the state, so start calculating the angle
            # and scale based on the corrected counter value.
            self.still = False
            
            # Make sure we calculate using floating point values
            self.angle = ((corrected_counter_value / (DeadState.ROTATION_TIME * 1.)) * 360) % 360
            
            self.scale = 1. - corrected_counter_value / (DeadState.ANIMATION_TIME * 1.) * self.scale_delta
        
        return 'dead'
    
    def get_image(self):
        """Returns the source image if we are still in still phase, otherwise returns
        a rotated and scaled image."""
        if self.still:
            return self.image
        else:
            surface = pygame.transform.rotozoom(self.image.get_surface(), self.angle, self.scale)
            offset_x, offset_y = self.image.get_offset()
            offset_x /= self.scale / 2
            offset_y /= self.scale / 2
            return Image(surface, (offset_x, offset_y))
            