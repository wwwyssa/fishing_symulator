import random
import pygame
import pygame_gui

import variables
from constants import WIDTH, HEIGHT, STEP_TEXT, INDENT, FISH_COUNT, FPS, SIZE, SCILL, BEACH_BOTTOM
from fish import Fish
from pause import pause
from util import load_image, write_text


def is_good_coord(a, b):
    print(a, b)
    return abs(a - b) <= SCILL


def money_upd(screen):
    font = pygame.font.Font(None, 60)
    string_rendered = font.render(f'Баланс: {variables.MONEY}', 1, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = 0
    intro_rect.x = WIDTH / 2 - string_rendered.get_width() / 2
    pygame.draw.rect(screen, '#d39353', (0, intro_rect.top, WIDTH, BEACH_BOTTOM))
    screen.blit(string_rendered, intro_rect)


def get_fish(position, *groups):
    for fish in groups[0]:
        if is_good_coord(fish.rect.center[0], position[0]) and is_good_coord(fish.rect.center[1], position[1]):
            return fish.catch(), fish.cost
        print()
    return 0, 0


def create_fish(position, *groups):
    Fish(position[0], position[1], *groups)


def start_game(screen):
    fon = pygame.transform.scale(load_image('Sky_Blue.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    all_sprites = pygame.sprite.Group()

    for i in range(FISH_COUNT):
        create_fish((random.randint(0, WIDTH), random.randint(BEACH_BOTTOM, HEIGHT)), all_sprites)
    manager = pygame_gui.UIManager(SIZE)
    pause_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH - 60, 0), (50, 50)),
        text='▐▐',
        manager=manager,
    )
    clock = pygame.time.Clock()
    can_fishing = 0
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and can_fishing <= 0:
                # create_fish((random.randint(0, WIDTH), random.randint(0, HEIGHT)), all_sprites)
                can_fishing, cost = get_fish(event.pos, all_sprites)
                variables.MONEY += cost
                print(can_fishing, variables.MONEY)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == pause_button:
                        if pause(screen) == 0:
                            fon = pygame.transform.scale(load_image('start_fon.jpg'), SIZE)
                            screen.blit(fon, (0, 0))
                            write_text(screen, ["Рыбалка"], STEP_TEXT)
                            return
            manager.process_events(event)
        all_sprites.update()
        screen.blit(fon, (0, 0))
        money_upd(screen)
        manager.update(time_delta)
        manager.update(FPS)
        manager.draw_ui(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        can_fishing -= 1
    pygame.quit()
