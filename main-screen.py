import pygame
import random
import math
from simulation import *
from constants import *

# pygame setup
screen = pygame.display.set_mode((MAIN_SCREEN_WIDTH, MAIN_SCREEN_HEIGHT))
vector = pygame.math.Vector2

def main():
    pygame.display.set_caption('Simulation of people moving')
    clock = pygame.time.Clock()
    simulation1 = Simulation(True, False)
    simulation2 = Simulation(False, True)
    simulations = pygame.sprite.Group(simulation1, simulation2)

    running = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulations.update()
        screen.fill(WHITE)
        simulations.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()