from tile import Tile

class Door(Tile):
    def __init__(self, position):
        """Creates a new Door tile."""        
        Tile.__init__(self, 'door', position)