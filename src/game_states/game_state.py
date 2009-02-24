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
class GameState():
    """Abstract parent class for game states. GameState implementations should implement
    at least these methods:
    
        - update(self, time_passed): Updates the state of the game's objects and returns
          the name of the next state as a string.
        - render(self, screen): Renders the game objects that need to be rendered.
    """
    
    def __init__(self, game):
        """Initializes a new game state. Stores a reference to the Game object for
        later access and creates an emtpy event queue."""
        self.game = game
        
        self.events = []
    
    def render(self, screen):
        """Default implementation for the render method. Renders the world and the HUD."""
        self.game.world.render(screen)
        self.game.hud.render(screen)
    
    def enter(self, previous_state):
        """Called when entering this state. This allows for initialization when entering
        the state. By default does nothing."""
        pass
    
    def exit(self, next_state):
        """Called when exiting this state. Can be used to restore settings that have
        been altered upon entering the state. By default does nothing."""
        pass
    
    def add_event(self, event):
        """Adds an event to the state's internal event queue."""
        self.events.append(event)
    
    def get_events(self):
        """Returns the list of events and clears the internal one."""
        events = self.events
        self.events = []
        return events