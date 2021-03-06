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
from animation import Animation
from enemy import Enemy
from game_entity import GameEntity

from states.enemies.krush.walking import WalkingState as KrushWalkingState
from states.enemies.krush.flat import FlatState as KrushFlatState
from states.enemies.turtle.walking import WalkingState as TurtleWalkingState
from states.enemies.turtle.shell import ShellState as TurtleShellState
from states.enemies.turtle.shell_moving import ShellMovingState as TurtleShellMovingState

class Krush(Enemy):
    def __init__(self, position, map):
        Enemy.__init__(self, position, (64, 52), map)
        
        self.rect.move_ip(0, 6)
        
        self.states = {
            'walk': KrushWalkingState(self),
            'flat': KrushFlatState(self)
        }
        self.currentState = self.states['walk']

class Turtle(Enemy):
    def __init__(self, position, map):
        Enemy.__init__(self, position, (64, 64), map)
        
        self.states = {
            'walk': TurtleWalkingState(self),
            'shell': TurtleShellState(self),
            'shell_moving': TurtleShellMovingState(self)
        }
        self.currentState = self.states['walk']