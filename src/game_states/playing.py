from pygame.locals import *
from src.game_locals import *

from src.game_states.game_state import GameState

class PlayingState(GameState):
    """State to represent a game that is currently active, allowing for user interaction
    with the player entity.
    """
    
    def __init__(self, *args):
        GameState.__init__(self, *args)
        
        self.debug = False
    
    def update(self, tick_data):
        next_state = 'playing'
        
        for event in self.get_events():
            if event.type == PLAYER_DEATH:
                next_state = 'player_death'
            elif event.type == MAP_FINISHED:
                next_state = 'map_transition'
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    if self.debug:
                        self.debug = False
                    else:
                        self.debug = True
                if event.key == K_r:
                    self.game.reset_world()
                if event.key == K_ESCAPE and next_state is 'playing':
                    next_state = 'paused'
        
        tick_data['debug'] = self.debug
        
        self.game.world.update(tick_data)
        self.game.hud.update(tick_data)
        
        return next_state