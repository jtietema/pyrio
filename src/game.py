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
        self.state = 'playing'
        self.get_current_state().enter(None)
        
        self.map_package = MapPackage('testpak')
    
    def get_current_state(self):
        """Returns the current state object. Useful since the current state is stored
        in string form on the game object."""
        return self.states[self.state]

    def create(self):
        self.world = self.map_package.current()
        self.hud = Hud()
        self.menu = Menu()
        
    def run(self):
        pygame.init()

        display_info = pygame.display.Info()
        screen = pygame.display.set_mode((display_info.current_w, display_info.current_h),
            DOUBLEBUF | HWSURFACE | FULLSCREEN, 32)
        #screen = pygame.display.set_mode((800,600),0,32)
        pygame.display.set_caption('Pyrio')
        pygame.mouse.set_visible(False)

        clock = pygame.time.Clock()
        
        self.create()

        actions = Actions()

        # setup joystick/gamepad if present
        joystick = None
        if pygame.joystick.get_count() > 0:
            # at least one joystick is found
            print str(pygame.joystick.get_count()) + ' joystick(s) found'
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            print 'Joystick found with ' + str(joystick.get_numaxes()) + ' axes and ' + str(joystick.get_numbuttons()) + ' buttons'

        while True:
            # Get the current state object.
            state = self.get_current_state()
            
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
                state.add_event(event)
            
            # Default values for tick data items.
            time_passed = clock.tick()
            tick_data['time_passed'] = time_passed
            tick_data['actions'] = self.process_controls(actions, joystick)
            tick_data['screen_size'] = screen.get_size()
            tick_data['score'] = self.score
            tick_data['lives'] = self.lives
            
            tick_data['debug'] = False # TODO: move to config!!!

            next_state = state.update(tick_data)
            
            # Make sure we have received a string as the return value from the
            # previous update() call to the current state.
            assert isinstance(next_state, str)

            # Store some tick data items on the Game object, so they can be stored
            # across multiple render cycles and are not reset upon the next cycle.
            self.score = tick_data['score']
            
            state.render(screen)
            
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
        if next_state is not self.state:
            self.switch_state(next_state)
    
    def switch_state(self, next_state):
        """Switches to a different state, appropriately calling exit() on the current
        state and enter() on the new state."""
        previous_state = self.state
        self.get_current_state().exit(next_state)
        self.state = next_state
        self.get_current_state().enter(previous_state)
            
    def reset_world(self):
        self.world = self.map_package.current()

    def process_controls(self, actions, joystick):
        """
        Maps all the supported controls to a common format.
        """
        actions.reset()
        # process the keyboard controls
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            actions.set_jump(True)

        if pressed_keys[K_LEFT]:
            actions.set_x(-1.0)

        if pressed_keys[K_RIGHT]:
            actions.set_x(1.0)

        if pressed_keys[K_UP]:
            actions.set_y(1.0)

        if pressed_keys[K_DOWN]:
            actions.set_y(-1.0)

        if pressed_keys[K_RETURN]:
            actions.set_select(True)
        
        if pressed_keys[K_ESCAPE]:
            actions.set_cancel(True)

        # process gamepad / joystick
        if joystick is not None:
            if joystick.get_button(0):
                actions.set_jump(True)
            if joystick.get_button(1):
                actions.set_select(True)
            if joystick.get_axis(0) > .05 or joystick.get_axis(0) < -.05:
                actions.set_x(joystick.get_axis(0))
            if joystick.get_axis(1) > .05 or joystick.get_axis(1) < -.05:
                actions.set_y(-1 * joystick.get_axis(1))
        
        return actions

    def get_lives(self):
        return self.lives
