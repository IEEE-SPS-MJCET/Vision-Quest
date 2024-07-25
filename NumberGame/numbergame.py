import pygame
import random
from setting import *

# Initialize Pygame's font module
pygame.font.init()

# Define a font object for rendering numbers
font = pygame.font.Font(None, 80)  # You can specify a font file and size

class PositiveNumber:
    def __init__(self):
        self.value = random.randint(1, 10)  # Positive value
        size = (50, 50)
        moving_direction, start_pos = self.define_spawn_pos(size)
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0], size[1])
        self.text_surface = font.render(str(self.value), True, (0, 255, 0))  # Green text for positive numbers

    def define_spawn_pos(self, size):
        vel = random.uniform(MOVE_SPEED["min"], MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [vel, 0]
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [-vel, 0]
        if moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT+size[1])
            self.vel = [0, -vel]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
            self.vel = [0, vel]
        return moving_direction, start_pos

    def move(self):
        self.rect.move_ip(self.vel)

    def draw(self, surface):
        surface.blit(self.text_surface, self.rect.topleft)

    def kill(self, numbers):
        numbers.remove(self)
        return self.value

class NegativeNumber:
    def __init__(self):
        self.value = random.randint(-10, -1)  # Negative value
        size = (50, 50)
        moving_direction, start_pos = self.define_spawn_pos(size)
        self.rect = pygame.Rect(start_pos[0], start_pos[1], size[0], size[1])
        self.text_surface = font.render(str(self.value), True, (255, 0, 0))  # Red text for negative numbers

    def define_spawn_pos(self, size):
        vel = random.uniform(MOVE_SPEED["min"], MOVE_SPEED["max"])
        moving_direction = random.choice(("left", "right", "up", "down"))
        if moving_direction == "right":
            start_pos = (-size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [vel, 0]
        if moving_direction == "left":
            start_pos = (SCREEN_WIDTH + size[0], random.randint(size[1], SCREEN_HEIGHT-size[1]))
            self.vel = [-vel, 0]
        if moving_direction == "up":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), SCREEN_HEIGHT+size[1])
            self.vel = [0, -vel]
        if moving_direction == "down":
            start_pos = (random.randint(size[0], SCREEN_WIDTH-size[0]), -size[1])
            self.vel = [0, vel]
        return moving_direction, start_pos

    def move(self):
        self.rect.move_ip(self.vel)

    def draw(self, surface):
        surface.blit(self.text_surface, self.rect.topleft)

    def kill(self, numbers):
        numbers.remove(self)
        return self.value
