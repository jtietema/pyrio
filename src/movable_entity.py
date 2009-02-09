
from game_entity import GameEntity

class MovableEntity(GameEntity):
    def __init__(self, (x,y), (width, height), map):
        GameEntity.__init__(self, (x,y), (width, height))

        self.falling = False
        self.map = map

    def check_falling(self, y_delta):
        return not self.map.collisions(self, (0, y_delta))

    def update(self, tick_data):        
        previous_animation = self.animation

        self.process(tick_data)

        if self.animation is not previous_animation:
            # Reset the state timer if the state was changed
            self.animation.reset()

        self.animation.process(tick_data['time_passed'])
    
    def render(self, screen, position):
        GameEntity.render(self, screen, self.animation.get_image(), position)