"""
This file is part of Pyrio.

Pyrio is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Pyrio is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Pyrio.  If not, see <http://www.gnu.org/licenses/>.
"""
import pygame

import assets

class Hud():
    def __init__(self):
        # image to be rendered
        self.livesImage = assets.images.game.lives
        self.scoreImage = assets.images.game.score
        self.font = pygame.font.SysFont('default', 56)

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
        text_surface = self.font.render(str(self.score), True, (255,255,0))
        score_width = text_surface.get_size()[0]
        screen.blit(text_surface, ((width - score_width - 80), 10))
        
