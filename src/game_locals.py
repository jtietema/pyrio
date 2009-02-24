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
from pygame.locals import *

# Events constants
PLAYER_DEATH = USEREVENT + 1
DEATH_ANIMATION_DONE = USEREVENT + 2
MAP_FINISHED = USEREVENT + 3
COIN_COLLECTED = USEREVENT + 4
VIDEOMODE_CHANGED = USEREVENT + 5