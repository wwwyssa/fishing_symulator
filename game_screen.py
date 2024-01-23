import random
import pygame

from constants import WIDTH, HEIGHT, STEP_TEXT, INDENT, FISH_COUNT, FPS, SIZE, SCILL, LINE_COLOR, LINE_WIDTH
from fish import Fish
from util import load_image


def is_good_coord(a, b):
    print(a, b)
    return abs(a - b) <= SCILL


def get_fish(position, *groups):
    for fish in groups[0]:
        if is_good_coord(fish.rect.center[0], position[0]) and is_good_coord(fish.rect.center[1], position[1]):
            return fish, fish.catch(), fish.cost
    return None, 0, 0


def create_fish(position, *groups):
    Fish(position[0], position[1], *groups)


def start_game(screen):
    fon = pygame.transform.scale(load_image('Sky_Blue.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    all_sprites = pygame.sprite.Group()
    for i in range(FISH_COUNT):
        create_fish((random.randint(0, WIDTH), random.randint(0, HEIGHT)), all_sprites)

    cursor_img = pygame.transform.scale(load_image("cursor_img_float.png"), (20, 120))
    cursor_img_rect = cursor_img.get_rect()
    hook_img = pygame.transform.scale(load_image("hook_img.png"), (25, 42))
    hook_img_rect = cursor_img.get_rect()

    clock = pygame.time.Clock()
    time_fishing = 0
    running = True
    pygame.mouse.set_visible(False)
    fish = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and fish is None:
                # create_fish((random.randint(0, WIDTH), random.randint(0, HEIGHT)), all_sprites)
                fish, time_fishing, cost = get_fish(event.pos, all_sprites)

        all_sprites.update()
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)

        if fish is None:
            cursor_img_rect.center = pygame.mouse.get_pos()
            screen.blit(cursor_img, cursor_img_rect)
        else:
            hook_img_rect = fish.get_pos()
            pygame.draw.line(screen, LINE_COLOR, (0, 0), fish.get_pos(), LINE_WIDTH)
            screen.blit(hook_img, hook_img_rect)

        pygame.display.flip()

        clock.tick(FPS)
        time_fishing -= 1
        if time_fishing <= 0:
            fish = None

    pygame.quit()
