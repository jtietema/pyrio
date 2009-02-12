
from src.game_entity import GameEntity

class State():
    def __init__(self, entity, animations, x_speed=0, y_speed=0):
        self.animations = animations
        self.x_speed = x_speed
        self.y_speed = y_speed
        # reference to the parent entity
        self.entity = entity

    def get_animation(self, direction):
        """Returns the animation object based on the entity's direction passed in.
        This should be overwritten if animations are named other than 'left' and 'right'.
        Also, consider using caching the current animation if you implement complex logic
        here, as this method is called multiple times per frame."""
        if direction is GameEntity.DIRECTION_LEFT:
            return self.animations['left']
        else:
            return self.animations['right']

    def update(self, tick_data):
        return self.process(tick_data)

    def enter(self):
        """Resets the state to its starting point. Automatically called by MovableEntity
        when switching states."""
        pass
    
    def exit(self):
        """Called when leaving the state."""
        pass
    
    def get_size(self):
        return self.entity.default_size
