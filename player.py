
import pygame

class Player():
    def __init__(self):
        self.image = None
        
    def update(self, tick_data):
        pass
        
    def render(self, screen):
        pygame.draw.rect(screen, (255,0,0), (380, 280, 40, 40))