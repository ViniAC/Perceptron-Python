import random
import pygame

black = 0, 0, 0


class Point:
    point = None
    x = None
    y = None
    label = None
    surface = None

    def __init__(self, width, height, surface):
        self.x = random.randrange(width)
        self.y = random.randrange(height)
        self.surface = surface
        if (self.x > self.y):
            self.label = 1
        else:
            self.label = -1

    def show(self):
        if (self.label == 1):
            self.point = pygame.draw.circle(self.surface, black, [
                               self.x, self.y], 10, 2)
        else:
            self.point = pygame.draw.circle(self.surface, black, [
                               self.x, self.y], 10)
