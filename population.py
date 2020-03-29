import pygame
import random
import math
from individual import *
from constants import *

class Population(pygame.sprite.Sprite):
    def __init__(self, bg_color, start_x, end_x, start_y, end_y, individuals=[], is_lockdown_mode=False):
        pygame.sprite.Sprite.__init__(self)

        self.individuals = individuals
        
        # simulation configs
        self.bg_color = bg_color
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.is_lockdown_mode = is_lockdown_mode
        self.percentage_chance = 10 if is_lockdown_mode else 20
        self.dict_collisions = {}
        
        # pygame configs
        self.image = pygame.Surface((end_x - start_x, end_y - start_y))
        self.image.fill(self.bg_color)
        self.rect = self.image.get_rect(left=start_x, top=start_y)
        self.stuff = pygame.sprite.Group(self.individuals)

    def update(self):
        self.stuff.update()
        self.image.fill(self.bg_color)
        self.stuff.draw(self.image)

    def check_individual_collision(self, individual):
        for indiv in self.individuals:
            if individual.id != indiv.id:
                if self.dict_collisions.get(str(individual.id)) != indiv.id:
                    self.dict_collisions[str(individual.id)] = indiv.id
                if individual.velocity.distance_to(indiv.velocity) < RADIUS*2 and indiv.is_infected and random.randint(1,100) < self.percentage_chance:
                    individual.set_color(RED)
                    individual.is_infected = True

    def trigger_simulation(self):
        for individual in self.individuals:
            individual.check_wall_collision()
            self.check_individual_collision(individual)

