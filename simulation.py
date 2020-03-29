import pygame
import random
import math
from statistics import *
from population import *
from constants import *

class Simulation(pygame.sprite.Sprite):
    def __init__(self, left, is_lockdown_mode=False):
        pygame.sprite.Sprite.__init__(self)
        
        # simulation configs
        self.is_lockdown_mode = is_lockdown_mode
        self.individuals = []
        
        # pygame configs
        self.image = pygame.Surface((MAIN_SCREEN_WIDTH/2, MAIN_SCREEN_HEIGHT))
        self.image.fill(WHITE)
        self.populationCanvas = pygame.Surface((SIMULATION_END_X - SIMULATION_START_X, SIMULATION_HEIGHT + 10 - 5)) # cheat
        self.feed_simulation()
        self.rect = self.image.get_rect(left=0 if left else MAIN_SCREEN_WIDTH/2)
        self.population = Population(LIGHTGRAY, SIMULATION_START_X, SIMULATION_END_X, 5, SIMULATION_HEIGHT + 10, self.individuals, self.is_lockdown_mode)
        self.statistics = Statistics(WHITE, SIMULATION_START_X, SIMULATION_END_X, SIMULATION_HEIGHT + 20, MAIN_SCREEN_HEIGHT - 5)
        self.stuff = pygame.sprite.Group(self.population, self.statistics)

    def update(self):
        self.stuff.update()
        self.population.trigger_simulation()
        self.image.fill(WHITE)
        self.stuff.draw(self.image)
    
    def feed_simulation(self):
        for n in range(INITIAL_HEALTHY_INDIVIDUAL):

            x_rand = random.randint(SIMULATION_START_X + PADDING, SIMULATION_WIDTH)
            y_rand = random.randint(SIMULATION_START_X + PADDING, SIMULATION_HEIGHT)

            is_moving = n <= INITIAL_INFEECTED_INDIVIDUAL if self.is_lockdown_mode else True 
            individual = Individual(n, x_rand, y_rand, RADIUS, random.uniform(0, math.pi*2), self.populationCanvas, n <= INITIAL_INFEECTED_INDIVIDUAL, is_moving)
            individual.angle = random.uniform(0, math.pi*2)

            self.individuals.append(individual)