
from asset_manager import AssetManager
from game_entity import GameEntity

class Animation():
    def __init__(self, image_group, images, frame_length=GameEntity.FRAME_LENGTH):
        # Counter to hold the total number of milliseconds passed since the start.
        # Please note that this counter is reset when its value gets too high or too low.
        self.counter = 0
        
        # The direction the animation is traversing its images. 1 for left to right
        # (or lower to higher index in the images list), -1 for right to left (higher
        # to lower). This is used for 
        self.direction = 1
        
        # The length of one frame of the animation in milliseconds
        self.frame_length = frame_length
        
        # Load the images for this animation
        self.images = []
        for name in images:
            self.images.append(AssetManager.get_image(image_group, name))

        self.image = self.images[0]
        
        # Image number counter cache.
        self.num_images = len(self.images)
        
        # The maximum value the frame counter should reach. We calculate this to prevent
        # the counter's value to become very large over time.
        self.counter_max = self.num_images * self.frame_length - 1
    
    def process(self, time_passed):
        """Determines the current image of the animation to display based on the time
        passed since the previous call. Corrects for overflow or underflow of the counter
        and automatically flips the direction of the image traversal if either occurs."""
        if self.num_images is 1:
            # No point in calculating the current image if there is only one image.
            self.image = self.images[0]
        else:
            # Store the increase in milliseconds.
            self.counter += self.direction * time_passed
            
            while True:
                if self.counter > self.counter_max:
                    # Counter passed its maximum value. Flip the direction of the image
                    # traversal and correct for the counter overflow that occurred.
                    overflow = self.counter - self.counter_max
                    self.counter = self.counter_max - (self.frame_length + overflow)
                    self.direction = -1
                elif self.counter < 0:
                    # Counter passed its minimum value (zero). Flip the direction and
                    # correct for the underflow that occurred.
                    underflow = abs(self.counter)
                    self.counter = self.frame_length + underflow
                    self.direction = 1
                else:
                    # Milliseconds counter has a valid value.
                    break

            # Determine the current image based on the milliseconds counter's value.
            self.image = self.images[self.counter // self.frame_length]
    
    def reset(self):
        """Resets the animation's internal milliseconds counter back to zero, effectively
        resetting the animation to its start point."""
        self.counter = 0
    
    def get_image(self):
        """Returns the current image (pygame Surface object) of the animation."""
        return self.image