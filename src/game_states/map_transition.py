from src.game_states.game_state import GameState
from src.overlay import Overlay

class MapTransitionState(GameState):
    """State used for transitions between maps. Also used on initial load of the first
    map."""
    
    def update(self, tick_data):
        """Updates no entities, since we want to want everything to be stale and simply
        perform a fade-out/fade-in."""        
        time_passed = tick_data['time_passed']
        self.overlay.update(time_passed)
        
        if self.done:
            return 'playing'
        
        return 'map_transition'
    
    def render(self, screen):
        GameState.render(self, screen)
        
        self.overlay.render(screen)
        
    def enter(self, previous_state):        
        self.overlay = Overlay(fade_speed=500)
        self.overlay.register_fade_in_listener(self)
        self.overlay.register_fade_out_listener(self)
        
        self.overlay.set_opacity(0)
        self.overlay.fade_in()
        self.done = False
    
    def exit(self, next_state):
        del self.overlay
    
    def overlay_fade_in_done(self, overlay):
        """Called by the overlay when it is done fading in. Loads the next map and flips
        the overlay to fade out again."""        
        self.game.next_map()
        overlay.fade_out()
    
    def overlay_fade_out_done(self, overlay):
        """Called by the overlay when it is done fading in."""
        self.done = True