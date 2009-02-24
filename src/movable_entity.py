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
        
        # Remember last state to detect state change.
        previous_state = self.currentState
        
        # Update the current state and store the state to move to.
        next_state = self.currentState.update(tick_data)
        
        # Change the current state to the new one, reset the state if a
        # new one has been set.
        next_state = self.states[next_state]
        if next_state is not previous_state:
            previous_state.exit()
            next_state.enter()
            self.currentState = next_state

        # check for debug mode
        self.debug = tick_data['debug']
    
    def render(self, screen, map_offsets):
        GameEntity.render(self, screen, self.currentState.get_image(), map_offsets)
    
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
    
    def switch_state(self, target_state):
        """Switches to the passed in state. Takes care of calling the exit and enter
        hook methods."""
        self.currentState.exit()
        self.currentState = self.states[target_state]
        self.currentState.enter()