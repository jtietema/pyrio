import pygame

class Overlay():
    """Class to represent an overlay drawn over the screen. The fading task can be set
    using the fade_in(), fade_out() and stop_fade() methods. Please note that fading
    only works if the overlay's update() method is called in the main game loop.
    
    If the overlay reaches fully transparent state when fading out, or fully opaque
    state when fading in, stop_fade() is automatically called."""
    
    FADING_IN = 1
    FADING_OUT = -1
    NOT_FADING = 0
    
    MAX_ALPHA = 255
    
    def __init__(self, opacity=50, fade_speed=1000):
        """Initializes a new overlay object."""
        # Create a new black surface the size of the screen.
        self.surface = pygame.Surface((1920, 1200))
        self.surface.fill((0, 0, 0))
        
        # By default, do not fade.
        self.fading = Overlay.NOT_FADING
        
        self.fade_speed = fade_speed
        
        # Opacity of the overlay in percents.
        self.set_opacity(opacity)
        
        # Lists to hold listeners
        self.fade_in_listeners = []
        self.fade_out_listeners = []
    
    def set_opacity(self, opacity):
        """Sets the current opacity for this overlay."""
        self.opacity = opacity
        self.surface.set_alpha(self.get_alpha_value())
    
    def get_opacity(self):
        """Returns the current opacity."""
        return self.opacity
    
    def get_alpha_value(self):
        """Calculates the alpha value based on the opacity."""
        return (self.opacity / 100) * Overlay.MAX_ALPHA
    
    def fade_in(self):
        """Sets the overlay to start fading in."""
        self.fading = Overlay.FADING_IN
    
    def fade_out(self):
        """Sets the overlay to start fading out."""
        self.fading = Overlay.FADING_OUT
    
    def stop_fade(self):
        """Stop fading."""
        self.fading = Overlay.NOT_FADING
    
    def get_fading_task(self):
        """Returns the fading task this overlay is currently executing."""
        return self.fading
    
    def render(self, screen):
        """Renders the overlay using the opacity to calculate the alpha value of the
        surface."""
        screen.blit(self.surface, (0, 0))
    
    def update(self, time_passed):
        """Updates the overlay's opacity based on the time passed."""
        if self.fading is Overlay.NOT_FADING:
            return
        
        opacity = self.get_opacity()
        opacity_delta = time_passed * 1. / self.fade_speed * 100
        
        if self.fading is Overlay.FADING_IN:
            opacity += opacity_delta
            opacity = min(100, opacity)
            
            if opacity is 100:
                self.stop_fade()
                self.notify_fade_in_listeners()
        elif self.fading is Overlay.FADING_OUT:
            opacity -= opacity_delta
            opacity = max(0, opacity)
            
            if opacity is 0:
                self.stop_fade()
                self.notify_fade_out_listeners()
        
        self.set_opacity(opacity)
    
    def register_fade_in_listener(self, listener):
        """Registers a new listener to call when a fade in of this overlay is done."""
        self.fade_in_listeners.append(listener)
    
    def notify_fade_in_listeners(self):
        """Calls overlay_fade_in_done() on all the listeners registered for the fade in
        done hook."""
        for listener in self.fade_in_listeners:
            listener.overlay_fade_in_done(self)
    
    def register_fade_out_listener(self, listener):
        """Registers a new listener to call when a fade out of this overlay is done."""
        self.fade_out_listeners.append(listener)

    def notify_fade_out_listeners(self):
        """Calls overlay_fade_out_done() on all the listeners registered for the fade out
        done hook."""
        for listener in self.fade_out_listeners:
            listener.overlay_fade_out_done(self)