import pygame
import random
import math
from constants import *

class Statistics(pygame.sprite.Sprite):
    
    def __init__(self, bg_color, start_x, end_x, start_y, end_y):
        pygame.sprite.Sprite.__init__(self)

        # simulation configs
        self.bg_color = bg_color
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y

        # pygame configs
        self.image = pygame.Surface((end_x - start_x, end_y - start_y))
        self.image.fill(self.bg_color)
        self.rect = self.image.get_rect(left=start_x, top=start_y)
        
        # drawing axis
        self.axis_origin = (start_x, end_y - start_y - 10)
        self.axis_y_length = end_y - start_y - 10
        self.axis_x_length = end_x - start_x

        pygame.draw.line(self.image, BLACK, self.axis_origin, (end_x, end_y - start_y - 10), 1) # horizontal
        for i in range(int(math.floor(self.axis_x_length/AXIS_INTERVAL))):
            pygame.draw.line(self.image, BLACK, (start_x + AXIS_INTERVAL*i, self.axis_y_length - 5), (start_x + AXIS_INTERVAL*i, self.axis_y_length + 5), 1) # vertical
        
        pygame.draw.line(self.image, BLACK, (start_x, 10), self.axis_origin, 1) # vertical
        for i in range(int(math.floor(self.axis_y_length/AXIS_INTERVAL))):
            pygame.draw.line(self.image, BLACK, (start_x - 5, 10 + AXIS_INTERVAL*i), (start_x + 5, 10 + AXIS_INTERVAL*i), 1) # vertical

    # def update(self):
    