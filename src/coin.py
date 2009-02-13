# -*- coding: utf-8 -*-

from game_entity import GameEntity
from animation import Animation

class Coin(GameEntity):
    def __init__(self, (x,y)):
        GameEntity.__init__(self, (x,y), (30,30))
        self.animation = Animation(('goldpiece', 'yellow'), ('1','2','3','4','5','6','7','8','9','10'))
    
    def update(self, tick_data):
        self.animation.process(tick_data['time_passed'])
    
    def render(self, screen, offsets):
        GameEntity.render(self,screen, self.animation.get_image(), offsets)
    