
import pygame
from pygame.locals import *
from sys import exit

from world import World

class Game():
    def create_world(self):
        self.world = World()
        
    def update(self, tick_data):
        self.world.update(tick_data)
        
    def render(self, screen):
        self.world.render(screen)
        
    def run(self):
        pygame.init()

        display_info = pygame.display.Info()
        screen = pygame.display.set_mode((display_info.current_w, display_info.current_h),
            DOUBLEBUF | HWSURFACE | FULLSCREEN, 32)
        #screen = pygame.display.set_mode((800,600),0,32)
        pygame.display.set_caption('Pygame platform')
        pygame.mouse.set_visible(False)

        clock = pygame.time.Clock()
        
        self.create_world()
        actions = Actions()

        while True:
            tick_data = {}
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit()

            tick_data['time_passed'] = clock.tick()
            tick_data['actions'] = self.process_controls(actions)
            tick_data['screen_size'] = screen.get_size()

            self.update(tick_data)
            self.render(screen)

            pygame.display.flip()

    def process_controls(self, actions):
        """
        Maps all the supported controls to a common format.
        """
        actions.reset()

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            actions.set_jump(True)

        if pressed_keys[K_LEFT]:
            actions.set_x(-1.0)

        if pressed_keys[K_RIGHT]:
            actions.set_x(1.0)

        return actions

class Actions():
    """
    Simple class to hold all the actions the player can do.  In the rest of the game you
    are suppossed to use this class instead off reading the controls directly.
    """
    def __init__(self):
        self.x = 0
        self.jump = False

    def set_x(self, x):
        """
        Must be a float between 1 (right) and -1 (left)
        """
        self.x = x

    def set_jump(self, boolean):
        self.jump = boolean

    def reset(self):
        self.__init__()