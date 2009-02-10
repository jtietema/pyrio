
from pygame.locals import *

from movable_entity import MovableEntity
from game_entity import GameEntity
from animation import Animation

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

        self.jumping = False
        self.jumping_time = 0
        
        self.animations = {
            'stand_left': Animation('player', ('stand_left',)),
            'stand_right': Animation('player', ('stand_right',)),
            'walk_left': Animation('player', ('walk_left_1', 'walk_left_2'), 200),
            'walk_right': Animation('player', ('walk_right_1', 'walk_right_2'), 200),
            'fall_left' : Animation('player', ('fall_left', )),
            'fall_right': Animation('player', ('fall_right',)),
            'jump_left' : Animation('player', ('jump_left', )),
            'jump_right': Animation('player', ('jump_right',))
        }
        
        self.animation = self.animations['stand_right']
        self.direction = GameEntity.DIRECTION_RIGHT
        
    def process(self, tick_data):
        time_passed = tick_data['time_passed']
        x_delta = time_passed * self.x_speed
        
        pressed_keys = tick_data['pressed_keys']
        animation_name = 'walk'
        if pressed_keys[K_LEFT]:
            x_delta *= -1
            self.direction = GameEntity.DIRECTION_LEFT
            if self.x_speed < Player.MAX_X_SPEED:
                self.x_speed *= 1.007
        elif pressed_keys[K_RIGHT]:
            self.direction = GameEntity.DIRECTION_RIGHT
            if self.x_speed < Player.MAX_X_SPEED:
                self.x_speed *= 1.007
        else:
            x_delta = 0
            animation_name = 'stand'
            self.x_speed = Player.MIN_X_SPEED
        
        if pressed_keys[K_UP] and ((not self.falling and not self.jumping) or
                self.jumping) and not self.jumping_time > Player.MAX_JUMPING_TIME:
            self.jumping = True
        else:
            self.jumping = False
            self.jumping_time = 0
            y_delta = 0

        if self.jumping and self.y_speed is 0:
            self.y_speed = Player.MAX_Y_SPEED

        if self.jumping:
            if self.y_speed > self.MIN_Y_SPEED:
                self.y_speed /= 1.007
            y_delta = time_passed * self.y_speed * -1
            self.jumping_time += time_passed
            animation_name = 'jump'
            if self.jumping_time > Player.MAX_JUMPING_TIME:
                self.jumping = False
                self.jumping_time = 0
        elif self.y_speed is 0:
            self.y_speed = Player.MIN_Y_SPEED

        self.falling = self.check_falling(time_passed * self.y_speed)
        if not self.jumping and self.falling:
            y_delta = time_passed * self.y_speed
            if self.y_speed < Player.MAX_Y_SPEED:
                self.y_speed *= 1.1
            animation_name = 'fall'

        if not self.jumping and not self.falling:
            self.y_speed = 0

        # Execute the move if there are no collisions
        if (x_delta is not 0 or y_delta is not 0 ):
            if not self.map.collisions(self, (x_delta, y_delta)):
                self.rect = self.rect.move(x_delta, y_delta)
            elif not self.map.collisions(self, (0, y_delta)):
                self.rect = self.rect.move(0, y_delta)
            elif not self.map.collisions(self, (x_delta, 0)):
                self.rect = self.rect.move(x_delta, 0)

        if self.direction is GameEntity.DIRECTION_LEFT:
            animation = '%s_%s' % (animation_name, 'left')
        else:
            animation = '%s_%s' % (animation_name, 'right')
        self.animation = self.animations[animation]
        
    def render(self, screen):        
        x_screen = screen.get_width() / 2 - self.rect.width / 2
        y_screen = screen.get_height() / 2 - self.rect.height / 2
        offset_x, offset_y = self.animation.get_image().get_offset()
        screen.blit(self.animation.get_image().get_surface(), (x_screen + offset_x, y_screen + offset_y))
        
