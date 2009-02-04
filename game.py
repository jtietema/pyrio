
import pygame
from pygame.locals import *
from sys import exit

from world import World

class Game():
    def __init__(self):
        self.world = World()
        
    def update(self, state):
        self.world.update(state)
        
    def render(self, screen):
        self.world.render(screen)
    
    
    @classmethod
    def run(cls):
        pygame.init()

        screen = pygame.display.set_mode((800, 600), 0, 32)
        pygame.display.set_caption("Pygame platform")

        clock = pygame.time.Clock()
        
        game = Game()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            time_passed = clock.tick()

            game.update(time_passed)
            game.render(screen)

            pygame.display.update()
        