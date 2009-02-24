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
from src.animation import Animation
from src.states.enemies.moving import MovingState

import src.assets as assets

class ShellMovingState(MovingState):
    def __init__(self, enemy):
        animations = {
            'moving': Animation(assets.images.enemies.turtle, ('shell_move_1', 'shell_move_2', 'shell_move_3'), 100)
        }
        
        MovingState.__init__(self, enemy, animations, .5)

    def get_animation(self):
        return self.animations['moving']
    
    def process(self, tick_data):
        flipped = MovingState.process(self, tick_data)
        if flipped:
            assets.sounds.turtle.hit_shell.play()
        
        if self.entity.collides_with_player():
            self.entity.hit_player(tick_data)
        
        return 'shell_moving'
            
    def enter(self):
        MovingState.enter(self)
        
        self.entity.rect.size = (42, 36)
        self.entity.rect.move_ip(0, 28)

    def exit(self):
        MovingState.exit(self)
        
        self.entity.rect.size = self.entity.default_size
        self.entity.rect.move_ip(0, -28)