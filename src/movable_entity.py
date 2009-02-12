
from game_entity import GameEntity

class MovableEntity(GameEntity):
    """Abstract MovableEntity class. To create a new MovableEntity, overload the
    __init__ function and set at least the following attributes on the object:
    
        states: A dictionary of possible states.
        currentState: The current state of the entity.
    
    For simple entities, it should suffice to implement only the appropriate states."""
    
    def __init__(self, (x,y), (width, height), map):
        GameEntity.__init__(self, (x,y), (width, height))
        self.map = map
        
        self.default_size = (width, height)
        
        # Default direction of all entities to right.
        self.direction = GameEntity.DIRECTION_RIGHT
    
    def is_falling(self):
        return self.falling

    def check_falling(self, y_delta):
        """Returns true if the entity is currently supposed to fall, i.e. there are no
        downward collisions."""
        return not self.map.collisions(self, (0, y_delta))

    def get_map(self):
        return self.map
    
    def get_previous_rect(self):
        """Returns the entity's rectangle position before processing the new frame."""
        return self.previous_rect
    
    def update(self, tick_data):
        """Updates the entity's state by calling the current state's update method.
        Also takes care of resetting the state and/or the animation if applicable."""
        self.previous_rect = self.rect
        
        # Store previous animation for later access.
        previous_animation = self.get_animation()
        
        # Remember last state to detect state change.
        previous_state = self.currentState
        
        # Update the current state and store the state to move to.
        next_state = self.currentState.update(tick_data)
        
        # Change the current state to the new one, reset the state if a
        # new one has been set.
        self.currentState = self.states[next_state]
        if self.currentState is not previous_state:
            self.currentState.reset()
            size = self.currentState.get_size()
            self.set_size(size)
            
        # Get the new animation and check to see if it has changed.
        animation = self.get_animation()
        if animation is not previous_animation:
            animation.reset()
        
        animation.process(tick_data['time_passed'])

        # check for debug mode
        self.debug = tick_data['debug']
    
    def render(self, screen, map_offsets):
        GameEntity.render(self, screen, self.get_animation().get_image(), map_offsets)
    
    def get_animation(self):
        """Helper method to quickly access the current animation object for
        this entity."""
        return self.currentState.get_animation(self.direction)
    
    def move(self, x_delta, y_delta):
        """Only executes a move if there are no collisions with tiles. Corrects for moves
        that can be performed if only the x or the y movement can be performed.
        Returns true if a movement could be performed, returns false if not."""
        if x_delta is not 0 or y_delta is not 0:
            if not self.map.collisions(self, (x_delta, y_delta)):
                self.rect = self.rect.move(x_delta, y_delta)
                return True
            elif y_delta is not 0 and not self.map.collisions(self, (0, y_delta)):
                self.rect = self.rect.move(0, y_delta)
                return True
            elif x_delta is not 0 and not self.map.collisions(self, (x_delta, 0)):
                self.rect = self.rect.move(x_delta, 0)
                return True

        return False 