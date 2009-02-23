from pygame.locals import *
from src.game_locals import *

from src.game_states.game_state import GameState

class PlayerDeathState(GameState):
    def update(self, tick_data):
        next_state = 'player_death'
        
        for event in self.get_events():
            if event.type == DEATH_ANIMATION_DONE:
                self.game.lives -= 1
                
                # Reset the world.
                self.game.reset_world()
                
                next_state = 'playing'
        
        self.game.world.update_player(tick_data)
        self.game.hud.update(tick_data)
        
        return next_state