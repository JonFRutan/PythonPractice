import pygame
from position import Position

class GameObject:
    def __init__ (self, position, width, height, color, speed):
        self.position = position
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def update(self, action):
        if isinstance(action, tuple): #If tuple...
            self.position.x += action[0] * self.speed
            self.position.y += action[1] * self.speed

#    def update(self, x_change, y_change):
#        self.position.x += 1
#        self.position.y += 1
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position.x, self.position.y, self.width, self.height))
