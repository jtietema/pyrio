
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
        
        self.x_speed = Player.MIN_X_SPEED
        self.y_speed = Player.MIN_Y_SPEED
        self.falling = True

        self.direction = GameEntity.DIRECTION_RIGHT

        self.states = {
            'walking' : WalkingState(self),
            'standing': StandingState(self),
            'jumping' : JumpingState(self),
            'falling' : FallingState(self)
        }
        self.currentState = self.states['falling']
        self.animation = self.currentState.get_animation(self.direction)
        
    def process(self, tick_data):
        next_state = self.currentState.update(tick_data)
        self.animation = self.currentState.get_animation(self.direction)
        # remember last state to detect state change
        previous_state = self.currentState
        self.currentState = self.states[next_state]
        if self.currentState is not previous_state:
            self.currentState.reset()
        
    def render(self, screen):        
        x_screen = screen.get_width() / 2 - self.rect.width / 2
        y_screen = screen.get_height() / 2 - self.rect.height / 2
        offset_x, offset_y = self.animation.get_image().get_offset()
        screen.blit(self.animation.get_image().get_surface(), (x_screen + offset_x, y_screen + offset_y))
        
