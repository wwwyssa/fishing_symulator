import random

import pygame
import pygame_gui

import variables
from constants import FPS, STEP_TEXT, SIZE, fon_sound, WIDTH, HEIGHT, BUTTON_SIZE, EFFICIENCY
from dollar import Dollar
from terminate import terminate
from util import load_image, write_text, get_button_coord
from variables import CURRENT_MONEY, cur_rod, MONEY


def create_dollar(all_sprites, dollar_count=10):
    numbers = range(-5, 6)
    for _ in range(dollar_count):
        Dollar((random.randint(0, WIDTH), 0), random.choice(numbers), random.choice(numbers), all_sprites)


def finish_screen(screen):
    pygame.mouse.set_visible(True)

    variables.MONEY += int(variables.CURRENT_MONEY * EFFICIENCY[variables.cur_rod])
    intro_text = ["Рыбалка закончена!\n",
                  f"Ваш выигрыш: {variables.CURRENT_MONEY} * {EFFICIENCY[variables.cur_rod]}"
                  f" = {int(variables.CURRENT_MONEY * EFFICIENCY[variables.cur_rod])}\n",
                  f"Ваш баланс: {variables.MONEY}"]
    variables.CURRENT_MONEY = 0

    fon_sound.set_volume(0.0)
    fon_sound.play()

    fon = pygame.transform.scale(load_image('finish_fon.jpg'), SIZE)
    screen.blit(fon, (0, 0))

    write_text(screen, intro_text, STEP_TEXT)

    manager = pygame_gui.UIManager(SIZE)
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(6), BUTTON_SIZE),
        text='На главную',
        manager=manager,
    )

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    create_dollar(all_sprites)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        return
            manager.process_events(event)

        screen.blit(fon, (0, 0))

        create_dollar(all_sprites, 1)
        all_sprites.update()
        all_sprites.draw(screen)

        write_text(screen, intro_text, STEP_TEXT)

        manager.update(FPS)
        manager.draw_ui(screen)

        pygame.display.flip()
        clock.tick(FPS)
