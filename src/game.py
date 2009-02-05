
import pygame
from pygame.locals import *
from sys import exit

from world import World

class Game():
    def __init__(self):
        self.world = World()
        
    def update(self, tick_data):
        self.world.update(tick_data)
        
    def render(self, screen):
        self.world.render(screen)
    
    
    @classmethod
    def run(cls):
        pygame.init()

        screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption('Pygame platform')

        clock = pygame.time.Clock()
        
        game = cls()

        while True:
            tick_data = {}
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            tick_data['time_passed'] = clock.tick()
            tick_data['pressed_keys'] = pygame.key.get_pressed()
            tick_data['screen_size'] = screen.get_size()

            game.update(tick_data)
            game.render(screen)

            pygame.display.update()
        