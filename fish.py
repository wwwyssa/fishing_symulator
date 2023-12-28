import pygame


class Fish(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, picture, speed, *groups):
        super().__init__(*groups)
        self.image = picture
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.speed = speed
