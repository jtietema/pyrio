# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys

from game_locals import *
from world import World
from hud import Hud
from map_package import MapPackage
from actions import Actions
from menu.menu import Menu
from config import Config

from game_states.playing import PlayingState
from game_states.paused import PausedState
from game_states.player_death import PlayerDeathState

class Game():
    def __init__(self):
        self.lives = 3
        self.score = 0
        
        # Initialize the game states
        self.states = {
            'playing': PlayingState(self),
            'paused': PausedState(self),
            'player_death': PlayerDeathState(self)
        }
        self.state = self.states['playing']
        self.state.enter()
        
        self.map_package = MapPackage('testpak')

    def create(self):
        self.world = self.map_package.current()
        self.hud = Hud()
        self.menu = Menu()
        
    def run(self):
        pygame.init()
        
        config = Config.get_instance()
        screen = pygame.display.set_mode(config.get_resolution(),
            config.get_doublebuffer_bitwise() | 
            config.get_hardwareacceleration_bitwise() | 
            config.get_fullscreen_bitwise(),32)
        
        pygame.display.set_caption('Pygame platform')
        pygame.mouse.set_visible(False)

        clock = pygame.time.Clock()
        
        self.create()

        actions = Actions()

        while True:
            tick_data = {}

            # Event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == KEYDOWN:
                    if event.key == K_q:
                        exit()
                elif event.type == MAP_FINISHED:
                    self.next_map()
                
                # Make sure the current state also has access to this event.
                self.state.add_event(event)
            
            # Default values for tick data items.
            time_passed = clock.tick()
            tick_data['time_passed'] = time_passed
            tick_data['actions'] = actions.process_controls()
            tick_data['screen_size'] = screen.get_size()
            tick_data['score'] = self.score
            tick_data['lives'] = self.lives
            
            tick_data['debug'] = False # TODO: move to config!!!

            next_state = self.state.update(tick_data)
            
            # Make sure we have received a string as the return value from the
            # previous update() call to the current state.
            assert isinstance(next_state, str)

            # Store some tick data items on the Game object, so they can be stored
            # across multiple render cycles and are not reset upon the next cycle.
            self.score = tick_data['score']
            
            self.state.render(screen)
            
            self.next_state(next_state)

            pygame.display.flip()
    
    def next_map(self):
        """Loads the next map in the map package."""
        try:
            # Try to get a world object for the next map.
            self.world = self.map_package.next()
        except:
            # An exception is thrown when the end of the map package list is
            # reached. This means we have finished the map package and can
            # quit the game for now.
            print 'Game finished'
            sys.exit()
    
    def next_state(self, next_state):
        """Checks if we need to switch to a different state, and switches if yes."""
        if self.states[next_state] is not self.state:
            self.switch_state(next_state)
    
    def switch_state(self, next_state):
        """Switches to a different state, appropriately calling exit() on the current
        state and enter() on the new state."""
        self.state.exit()
        self.state = self.states[next_state]
        self.state.enter()
            
    def reset_world(self):
        self.world = self.map_package.current()

    def get_lives(self):
        return self.lives
