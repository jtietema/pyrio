class Actions():
    """
    Simple class to hold all the actions the player can do.  In the rest of the game you
    are suppossed to use this class instead off reading the controls directly.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.jump = False
        self.select = False

    def set_x(self, x):
        """Must be a float between 1 (right) and -1 (left)"""
        self.x = x

    def set_y(self, y):
        """Must be a float between 1 (right) and -1 (left)"""
        self.y = y

    def set_jump(self, boolean):
        self.jump = boolean

    def reset(self):
        self.__init__()

    def set_select(self, boolean):
        self.select = True