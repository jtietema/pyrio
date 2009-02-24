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
class Image():
    def __init__(self, surface, (offset_x, offset_y) = (0,0)):
        self.image = surface
        self.offset = (offset_x, offset_y)

    def get_surface(self):
        return self.image

    def get_offset(self):
        return self.offset

    def get_size(self):
        return self.image.get_size()
        