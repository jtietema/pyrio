
from ..game_entity import GameEntity

class State():
    def __init__(self, entity, animations, x_speed, y_speed):
        self.animations = animations
        self.x_speed = x_speed
        self.y_speed = y_speed
        # reference to the parent entity
        self.entity = entity

    def get_animation(self, direction):
        if direction is GameEntity.DIRECTION_LEFT:
            return self.animations['left']
        else:
            return self.animations['right']

    def update(self, tick_data):
        return self.process(tick_data)

    def move(self, x_delta, y_delta):
        # Execute the move if there are no collisions
        if (x_delta is not 0 or y_delta is not 0 ):
            if not self.entity.get_map().collisions(self.entity, (x_delta, y_delta)):
                self.entity.rect = self.entity.rect.move(x_delta, y_delta)
            elif not self.entity.get_map().collisions(self.entity, (0, y_delta)):
                self.entity.rect = self.entity.rect.move(0, y_delta)
            elif not self.entity.get_map().collisions(self.entity, (x_delta, 0)):
                self.entity.rect = self.entity.rect.move(x_delta, 0)

    def reset(self):
        pass
