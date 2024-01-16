import random

import pygame
import os

from constants import fish_descriptions, SCREEN_RECT, FISH_SIZE
from util import load_image


class Fish(pygame.sprite.Sprite):
    fish_types = os.listdir(path='./data/fish')
    fish_pictures = [{i: None for i in fish_types}, {i: None for i in fish_types}]

    def __init__(self, pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.type = random.randint(0, len(self.fish_types) - 1)
        self.orientation = random.randint(0, 1)
        fish = fish_descriptions[self.type]
        self.image_name = fish["image_name"]
        if self.fish_pictures[self.orientation][fish["image_name"]] is None:
            img = load_image(f'fish/{self.fish_types[self.type]}')
            self.fish_pictures[0][fish["image_name"]] = img
            img_copy = img.copy()
            self.fish_pictures[1][fish["image_name"]] = pygame.transform.flip(img_copy, True, False)
        if self.fish_pictures[self.orientation][fish["image_name"]] is not None:
            # self.image = pygame.transform.scale(self.fish_pictures[self.orientation][self.image_name], FISH_SIZE)
            self.image = self.fish_pictures[self.orientation][self.image_name]
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.speed = fish["speed"]
        self.cost = random.randint(*fish["cost"])

    def update(self):
        self.rect.x += self.speed[self.orientation]
        if not self.rect.colliderect(SCREEN_RECT):
            self.orientation ^= 1
            self.image = self.fish_pictures[self.orientation][self.image_name]