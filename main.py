#!/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit

from game import Game

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
