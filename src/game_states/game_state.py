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
    
    def enter(self):
        """Called when entering this state. This allows for initialization when entering
        the state. By default does nothing."""
        pass
    
    def exit(self):
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