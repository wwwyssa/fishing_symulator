import random
import pygame
import pygame_gui

import variables
from constants import WIDTH, HEIGHT, STEP_TEXT, INDENT, FISH_COUNT, FPS, SIZE, SCILL, LINE_COLOR, LINE_WIDTH, \
    BEACH_BOTTOM
from fish import Fish
from pause import pause
from terminate import terminate
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
            return fish, fish.catch(), fish.cost
    return None, 0, 0


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
        time_delta = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and fish is None:
                # create_fish((random.randint(0, WIDTH), random.randint(0, HEIGHT)), all_sprites)
                fish, time_fishing, cost = get_fish(event.pos, all_sprites)
                variables.MONEY += cost
                print(time_fishing, variables.MONEY)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == pause_button:
                        pygame.mouse.set_visible(True)
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
