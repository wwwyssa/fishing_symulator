import random

import pygame
import os

from constants import fish_descriptions, SCREEN_RECT
from util import load_image


class Fish(pygame.sprite.Sprite):
    fish_types = os.listdir(path='./data/fish')
    fish_pictures = {i: None for i in fish_types}

    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.type = random.randint(0, len(self.fish_types) - 1)
        fish = fish_descriptions[self.type]
        if self.fish_pictures[fish["image_name"]] is None:
            self.fish_pictures[fish["image_name"]] = load_image(f'fish/{self.fish_types[self.type]}')

        self.image = self.fish_pictures[fish["image_name"]]
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.speed = fish["speed"]
        self.cost = random.randint(*fish["cost"])

    def update(self):
        self.rect.x += self.speed
        if not self.rect.colliderect(SCREEN_RECT):
            self.kill()