
from src.game_entity import GameEntity

class State():
    def __init__(self, entity, animations, x_speed=0, y_speed=0):
        self.animations = animations
        self.x_speed = x_speed
        self.y_speed = y_speed
        # reference to the parent entity
        self.entity = entity

    def get_animation(self):
        """Returns the animation object based on the entity's direction passed in.
        This should be overwritten if animations are named other than 'left' and 'right'.
        Also, consider using caching the current animation if you implement complex logic
        here, as this method is called multiple times per frame."""
        if self.entity.direction is GameEntity.DIRECTION_LEFT:
            return self.animations['left']
        else:
            return self.animations['right']

    def update(self, tick_data):
        previous_animation = self.get_animation()
        
        next_state = self.process(tick_data)
        
        # Get the new animation and check to see if it has changed.
        animation = self.get_animation()
        if animation is not previous_animation:
            animation.reset()
        
        if animation is not None:
            animation.process(tick_data['time_passed'])
        
        return next_state

    def enter(self):
        """Resets the state to its starting point. Automatically called by MovableEntity
        when switching states."""
        animation = self.get_animation()
        if animation is not None:
            self.get_animation().reset()
    
    def exit(self):
        """Called when leaving the state."""
        pass
    
    def get_size(self):
        return self.entity.default_size

    def get_image(self):
        return self.get_animation().get_image()