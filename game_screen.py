import random
import pygame

from constants import WIDTH, HEIGHT, STEP_TEXT, INDENT, FISH_COUNT, FPS, SIZE, SCILL
from fish import Fish
from util import load_image


def is_good_coord(a, b):
    print(a, b)
    return abs(a - b) <= SCILL


def get_fish(position, *groups):
    for fish in groups[0]:
        if is_good_coord(fish.rect.center[0], position[0]) and is_good_coord(fish.rect.center[1], position[1]):
            return fish.catch()
        print()
    return 0


def create_fish(position, *groups):
    Fish(position[0], position[1], *groups)


def start_game(screen):
    fon = pygame.transform.scale(load_image('Sky_Blue.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    all_sprites = pygame.sprite.Group()
    for i in range(FISH_COUNT):
        create_fish((random.randint(0, WIDTH), random.randint(0, HEIGHT)), all_sprites)

    clock = pygame.time.Clock()
    can_fishing = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and can_fishing <= 0:
                # create_fish((random.randint(0, WIDTH), random.randint(0, HEIGHT)), all_sprites)
                can_fishing = get_fish(event.pos, all_sprites)
                print(can_fishing)

        all_sprites.update()
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        can_fishing -= 1

    pygame.quit()
