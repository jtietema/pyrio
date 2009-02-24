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
from game_entity import GameEntity
from movable_entity import MovableEntity

class Enemy(MovableEntity):
    def __init__(self, position, size, map):
        MovableEntity.__init__(self, position, size, map)
    
    def update(self, tick_data):
        MovableEntity.update(self, tick_data)
    
    def render(self, screen, map_offsets):
        MovableEntity.render(self, screen, map_offsets)
    
    def is_hit_by_player(self):
        """Detects if the enemy is hit by the player."""
        p_rect = self.player.get_previous_rect()
        return self.collides_with_player() and p_rect.y < self.player.get_rect().y
    
    def hit_player(self, tick_data):
        """Hits the player entity."""
        self.player.hit(tick_data)
    
    def bounce_player(self, tick_data):
        """Makes sure the player bounces upward, using this entity's top y to set the
        origin of the player's jump."""
        self.player.bounce(tick_data, self.rect.top)