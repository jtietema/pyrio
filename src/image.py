
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

    
