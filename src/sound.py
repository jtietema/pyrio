import pygame

class Sound:
    """Wraps a pygame Sound object, allowing for additional storage and volume
    manipulation."""
    
    def __init__(self, sound_file, max_volume):
        """Initializes a new Sound object."""
        self.sound = pygame.mixer.Sound(sound_file)
        self.max_volume = max_volume
        self.sound.set_volume(self.max_volume)

    def play(self, volume=1.):
        """Plays the sound file, taking the volume (value between 0 and 1) into account.
        Note that this volume is not stored in any way, and only affects this play call.
        """
        if volume > 0:
            self.sound.play().set_volume(volume)
        