import pygame

from src.states.state import State
from src.image import Image

class DeadState(State):
    # Time in milliseconds it takes to spin 360 degrees.
    ROTATION_TIME = 750
    
    # Time before the player starts spinning.
    STILL_TIME = 500
    
    # The amount of time the player animates. Aggregate this with STILL_TIME
    # to get the full time the player stays in dead state.
    ANIMATION_TIME = 3000
    
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
        return None
    
    def set_source_image(self, image):
        self.image = image
    
    def process(self, tick_data):
        self.counter += tick_data['time_passed']
        
        corrected_counter_value = self.counter - DeadState.STILL_TIME
        
        if corrected_counter_value > DeadState.ANIMATION_TIME:
            tick_data['restart_level'] = True
        elif corrected_counter_value >= 0:
            self.still = False
            
            # Make sure we calculate using floating point values
            self.angle = ((corrected_counter_value / (DeadState.ROTATION_TIME * 1.)) * 360) % 360
            
            self.scale = 1. - corrected_counter_value / (DeadState.ANIMATION_TIME * 1.) * self.scale_delta
        
        return 'dead'
    
    def get_image(self):
        if self.still:
            return self.image
        else:
            surface = pygame.transform.rotozoom(self.image.get_surface(), self.angle, self.scale)
            offset_x, offset_y = self.image.get_offset()
            offset_x /= self.scale / 2
            offset_y /= self.scale / 2
            return Image(surface, (offset_x, offset_y))
            