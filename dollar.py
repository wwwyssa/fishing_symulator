import random
import pygame

from constants import GRAVITY, SCREEN_RECT
from util import load_image


class Dollar(pygame.sprite.Sprite):
    dollar_img = []

    def __init__(self, pos, dx, dy, *groups):
        super().__init__(*groups)
        if not Dollar.dollar_img:
            Dollar.dollar_img = [load_image("dollar.png")]
            for scale in (30, 40, 50):
                Dollar.dollar_img.append(pygame.transform.scale(Dollar.dollar_img[0], (scale, scale)))

        self.image = random.choice(Dollar.dollar_img[1:])
        self.rect = self.image.get_rect()

        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos

        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(SCREEN_RECT):
            self.kill()
