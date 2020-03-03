import pygame
import sys
import Perceptron
import Training


pygame.init()
size = width, height = 800, 800
white = 255, 255, 255
screen = pygame.display.set_mode(size)
screen.fill(white)

point_list = []
for item in range(100):
    point_list.append(Training.Point(width,height, screen))
for item in point_list:
    item.show()

p = Perceptron.Perceptron()
pygame.draw.line(screen, (0, 0, 0), (0,0),(width,height))

training_index = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in point_list:
                inputs = (item.x, item.y)
                target = item.label
                p.train(inputs, target)
    for item in point_list:
        item.show()
    for item in point_list:
        target = item.label
        inputs = (item.x, item.y)
        guess = p.guess(inputs)
        if guess == target:
            pygame.draw.circle(screen, (0, 255, 0), [item.x, item.y], 4)
        else:
            pygame.draw.circle(screen, (255, 0 , 0), [item.x, item.y], 4)
    pygame.display.update()

