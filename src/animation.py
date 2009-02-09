
from asset_manager import AssetManager

class Animation():
    def __init__(self, image_group, images, frame_length):
        self.counter = 0
        
        self.frame_length = frame_length
        
        # Load the images for this state
        self.images = []
        for filename in images:
            self.images.append(AssetManager.get_image(image_group, filename))
        
        self.max_frame_length = len(self.images) * self.frame_length
    
    def process(self, time_passed):
        self.counter += time_passed
        
        if self.counter >= self.max_frame_length:
            self.reset()
        
        self.image = self.images[self.counter // self.frame_length]
    
    def reset(self):
        self.counter = 0
    
    def get_image(self):
        return self.image