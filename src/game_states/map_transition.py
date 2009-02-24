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

import pygame
import os

from src.game_states.game_state import GameState
from src.overlay import Overlay
from src.game_locals import *

class MapTransitionState(GameState):
    """State used for transitions between maps. Also used on initial load of the first
    map."""
    
    def update(self, tick_data):
        """Updates no entities, since we want to want everything to be stale and simply
        perform a fade-out/fade-in."""
        for event in self.get_events():
            if event.type == MAP_FINISHED_MUSIC_DONE:
                pygame.mixer.music.set_endevent()
                self.overlay.fade_in()
                
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
        
        pygame.mixer.music.load(os.path.join('assets', 'music', 'map_finished.ogg'))
        pygame.mixer.music.set_endevent(MAP_FINISHED_MUSIC_DONE)
        pygame.mixer.music.play(1)
        
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