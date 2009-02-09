
from asset_manager import AssetManager
from game_entity import GameEntity

class Animation():
    def __init__(self, image_group, images, frame_length=GameEntity.FRAME_LENGTH):
        self.counter = 0
        self.direction = 1
        
        self.frame_length = frame_length
        
        # Load the images for this state
        self.images = []
        for name in images:
            self.images.append(AssetManager.get_image(image_group, name))
        
        self.counter_max = len(self.images) * self.frame_length - 1
    
    def process(self, time_passed):
        if len(self.images) is 1:
            self.image = self.images[0]
        else:
            self.counter += self.direction * time_passed
            
            while True:
                if self.counter > self.counter_max:
                    overflow = self.counter - self.counter_max
                    self.counter = self.counter_max - (self.frame_length + overflow)
                    self.direction = -1
                elif self.counter < 0:
                    underflow = abs(self.counter)
                    self.counter = self.frame_length + underflow
                    self.direction = 1
                else:
                    break

            self.image = self.images[self.counter // self.frame_length]
    
    def reset(self):
        self.counter = 0
    
    def get_image(self):
        return self.image