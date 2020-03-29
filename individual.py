import pygame
import pygame.gfxdraw
import random
import math
from constants import *

vector = pygame.math.Vector2

class Individual(pygame.sprite.Sprite):
    
    # constructor
    def __init__(self, id, x, y, radius, angle, canvas, is_infected=False, is_moving=False):
        pygame.sprite.Sprite.__init__(self)

        # individual configs
        self.id = id
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 1
        self.velocity = vector(x, y)
        self.radius = radius
        self.color = (0, 0, 255)
        self.is_infected = is_infected
        self.is_moving = is_moving

        # Create the surface, give dimensions and set it to be transparent
        self.image = pygame.Surface([self.radius*2, self.radius*2])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.gfxdraw.aacircle(self.image, self.radius, self.radius, self.radius - 1, RED if self.is_infected else BLUE)
        pygame.gfxdraw.filled_circle(self.image, self.radius, self.radius, self.radius - 1, RED if self.is_infected else BLUE)
        
        # this rect determinies the position the ball is drawn
        self.rect = self.image.get_rect(x=self.velocity.x, y=self.velocity.y)
        self.canvas = canvas
    
    def update(self):
        if self.is_moving:
            self.velocity.x += self.speed * math.cos(self.angle)
            self.velocity.y += self.speed * math.sin(self.angle)
            self.rect = self.image.get_rect(x=self.velocity.x, y=self.velocity.y)

    def set_color(self, color):
        pygame.gfxdraw.aacircle(self.image, self.radius, self.radius, self.radius - 1, color)
        pygame.gfxdraw.filled_circle(self.image, self.radius, self.radius, self.radius - 1, color) 

    # keep individual inside frame
    def check_wall_collision(self):
        if self.velocity.x >= self.canvas.get_rect().width - PADDING  or self.velocity.x <= self.canvas.get_rect().x:
            self.angle = math.pi - self.angle

        if self.velocity.y <= self.canvas.get_rect().x or self.velocity.y >= self.canvas.get_rect().height - PADDING:
            self.angle = -self.angle
