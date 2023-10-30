import pygame
from sys import exit

pygame.init()
running = False

# Creating screen
screen = pygame.display.set_mode((400, 640))
pygame.display.set_caption("Flappy Bird")

# Game loop
while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()