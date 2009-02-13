
import pygame
from pygame.locals import *
import sys

from world import World
from hud import Hud
from menu import Menu
from map_package import MapPackage
from actions import Actions

class Game():
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.pause = True
        self.debug = False
        self.dead = False
        
        self.map_package = MapPackage('testpak')

    def create(self):
        self.world = self.map_package.current()
        self.hud = Hud()
        self.menu = Menu()
        
    def update(self, tick_data):
        if self.pause:
            self.menu.update(tick_data)
        else:
            self.world.update(tick_data)
            self.hud.update(tick_data)
        
    def render(self, screen):
        self.world.render(screen)
        self.hud.render(screen)
        if self.pause:
            self.menu.render(screen)
        
    def run(self):
        pygame.init()

        display_info = pygame.display.Info()
        screen = pygame.display.set_mode((display_info.current_w, display_info.current_h),
            DOUBLEBUF | HWSURFACE | FULLSCREEN, 32)
        #screen = pygame.display.set_mode((800,600),0,32)
        pygame.display.set_caption('Pygame platform')
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
            tick_data = {}
            
            # Event handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        if self.pause:
                            self.pause = False
                        else:
                            self.pause = True
                    if event.key == K_ESCAPE:
                        exit()
                    if event.key == K_d:
                        if self.debug:
                            self.debug = False
                        else:
                            self.debug = True

            # Default values for tick data items.
            tick_data['time_passed'] = clock.tick()
            tick_data['actions'] = self.process_controls(actions, joystick)
            tick_data['screen_size'] = screen.get_size()
            tick_data['score'] = self.score
            tick_data['lives'] = self.lives
            tick_data['dead'] = self.dead
            tick_data['restart_world'] = False
            tick_data['level_complete'] = False
            tick_data['pause'] = self.pause
            tick_data['debug'] = self.debug

            self.update(tick_data)

            # Store some tick data items on the Game object, so they can be stored
            # across multiple render cycles and are not reset upon the next cycle.
            self.score = tick_data['score']
            self.pause = tick_data['pause']
            self.dead = tick_data['dead']
            
            self.render(screen)
            
            # Check some parameters that are global to the game and can't be handled
            # in encapsulated objects.
            if tick_data['restart_world']:
                # Time to restart the world.
                if self.dead:
                    # The player was declared dead before, so subtract a life.
                    self.lives -= 1
                
                # Reset the world.
                self.reset_world()
                
                # Reset the dead parameter: after the world has been reset, the player
                # is alive again.
                self.dead = False
            elif tick_data['level_complete']:
                try:
                    # Try to get a world object for the next map.
                    self.world = self.map_package.next()
                except:
                    # An exception is thrown when the end of the map package list is
                    # reached. This means we have finished the map package and can
                    # quit the game for now.
                    print 'Game finished'
                    sys.exit()

            pygame.display.flip()
            
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
