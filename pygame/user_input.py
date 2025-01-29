import pygame
from position import Position #note: file names (position) will be lowercase, while objects (Position) will be uppercase

class UserInput:
    def __init__(self):
        self.keys = None
        self.mouse_pos = (0, 0)    

    def check(self):
        self.keys = pygame.key.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
