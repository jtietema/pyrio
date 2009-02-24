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
from src.game_entity import GameEntity
from src.states.state import State

class ShellState(State):
    def __init__(self, enemy):
        animations = {
            'shell': Animation(('enemies', 'turtle'), ('shell_front',))
        }
        
        State.__init__(self, enemy, animations)
    
    def get_animation(self):
        return self.animations['shell']
    
    def process(self, tick_data):
        if self.entity.collides_with_player():
            if self.entity.is_hit_by_player():
                self.entity.bounce_player(tick_data)
            
            if self.entity.get_rect().centerx < self.entity.player.get_rect().centerx:
                self.entity.direction = GameEntity.DIRECTION_LEFT
                
                # Make sure we don't bump into the shell in the next frame, when it is
                # deadly.
                self.entity.rect.right = min(self.entity.player.rect.left, self.entity.rect.right)
            else:
                self.entity.direction = GameEntity.DIRECTION_RIGHT
                
                # Make sure we don't bump into the shell in the next frame, when it is
                # deadly.
                self.entity.rect.left = max(self.entity.player.rect.right, self.entity.rect.left)
            
            return 'shell_moving'
            
        return 'shell'
    
    def enter(self):
        State.enter(self)
        
        self.entity.rect.size = (42, 36)
        self.entity.rect.move_ip(0, 28)
    
    def exit(self):
        State.exit(self)
        
        self.entity.rect.size = self.entity.default_size
        self.entity.rect.move_ip(0, -28)