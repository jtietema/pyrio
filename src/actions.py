# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

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
        self.cancel = False
        self.joystick = None
        
        # setup joystick/gamepad if present
        joystick = None
        if pygame.joystick.get_count() > 0:
            # at least one joystick is found
            print str(pygame.joystick.get_count()) + ' joystick(s) found'
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print 'Joystick found with ' + str(self.joystick.get_numaxes()) + \
             ' axes and ' + str(self.joystick.get_numbuttons()) + ' buttons'

    def set_x(self, x):
        """Must be a float between 1 (right) and -1 (left)"""
        self.x = x

    def set_y(self, y):
        """Must be a float between 1 (up) and -1 (down)"""
        self.y = y

    def set_jump(self, boolean):
        self.jump = boolean

    def reset(self):
        self.__init__()

    def set_select(self, boolean):
        self.select = True
    
    def set_cancel(self, boolean):
        self.cancel = True
    
    def process_controls(self):
        """
        Maps all the supported controls to a common format.
        """
        self.reset()
        # process the keyboard controls
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.set_jump(True)

        if pressed_keys[K_LEFT]:
            self.set_x(-1.0)

        if pressed_keys[K_RIGHT]:
            self.set_x(1.0)

        if pressed_keys[K_UP]:
            self.set_y(1.0)

        if pressed_keys[K_DOWN]:
            self.set_y(-1.0)

        if pressed_keys[K_RETURN]:
            self.set_select(True)
        
        if pressed_keys[K_ESCAPE]:
            self.set_cancel(True)

        # process gamepad / joystick
        if self.joystick is not None:
            if self.joystick.get_button(0):
                self.set_jump(True)
            if self.joystick.get_button(1):
                self.set_select(True)
            if self.joystick.get_axis(0) > .05 or self.joystick.get_axis(0) < -.05:
                self.set_x(self.joystick.get_axis(0))
            if self.joystick.get_axis(1) > .05 or self.joystick.get_axis(1) < -.05:
                self.set_y(-1 * self.joystick.get_axis(1))
        
        return self
        