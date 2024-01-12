import random
import pygame

from constants import WIDTH, HEIGHT, STEP_TEXT, INDENT, FISH_COUNT, FPS, SIZE
from fish import Fish
from util import load_image


def create_fish(position, *groups):
    print(position)
    Fish(position[0], position[1], *groups)


def start_game(screen):
    intro_text = ["Игра"]
    fon = pygame.transform.scale(load_image('Sky_Blue.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 60)
    text_coord = INDENT
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = (WIDTH - intro_rect.width) // 2
        text_coord += intro_rect.height + STEP_TEXT
        screen.blit(string_rendered, intro_rect)

    all_sprites = pygame.sprite.Group()
    for i in range(FISH_COUNT):
        create_fish((random.randint(0, WIDTH), random.randint(0, HEIGHT)), all_sprites)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                create_fish((random.randint(0, WIDTH), random.randint(0, HEIGHT)), all_sprites)

        all_sprites.update()
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

