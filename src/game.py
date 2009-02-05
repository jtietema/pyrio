
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

        screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('Pygame platform')

        clock = pygame.time.Clock()
        
        self.create_world()

        while True:
            tick_data = {}
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            tick_data['time_passed'] = clock.tick()
            tick_data['pressed_keys'] = pygame.key.get_pressed()
            tick_data['screen_size'] = screen.get_size()

            self.update(tick_data)
            self.render(screen)

            pygame.display.update()
        