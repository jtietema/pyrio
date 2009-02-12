
import pygame

from asset_manager import AssetManager

class Hud():
    def __init__(self):
        # image to be rendered
        self.livesImage = AssetManager.get_image('game','lives')
        self.scoreImage = AssetManager.get_image('game', 'score')

        # data needed from tick_data
        display_info = pygame.display.Info()
        self.screen_size = (display_info.current_w, display_info.current_h)
        self.lives = 0
        self.score = 0

    def update(self, tick_data):
        self.screen_size = tick_data['screen_size']
        self.lives = tick_data['lives']
        self.score = tick_data['score']

    def render(self, screen):
        width, height = self.screen_size
        # render lives
        for live in range(self.lives):
            screen.blit(self.livesImage.get_surface(), (20 * (live+1), 10))

        # render score
        screen.blit(self.scoreImage.get_surface(), (width - 64, 10))
        font = pygame.font.SysFont('default', 56)
        text_surface = font.render(str(self.score), True, (255,255,0))
        score_width = text_surface.get_size()[0]
        screen.blit(text_surface, ((width - score_width - 80), 10))
        
