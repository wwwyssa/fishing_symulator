import pygame
import pygame_gui

from constants import FPS, STEP_TEXT, SIZE, fon_sound, BUTTON_SIZE
from game_screen import start_game
from inventory_screen import inventory_screen
from settings_screen import settings_screen
from terminate import terminate
from util import load_image, write_text, get_button_coord


def start_screen(screen):
    intro_text = ["Рыбалка"]

    fon_sound.set_volume(0.0)
    fon_sound.play()

    fon = pygame.transform.scale(load_image('start_fon.jpg'), SIZE)
    screen.blit(fon, (0, 0))

    write_text(screen, intro_text, STEP_TEXT)

    manager = pygame_gui.UIManager(SIZE)
    clock = pygame.time.Clock()

    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(3), BUTTON_SIZE),
        text='СТАРТ',
        manager=manager
    )

    inventory_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(4), BUTTON_SIZE),
        text='ИНВЕНТАРЬ',
        manager=manager

    )

    settings_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(5), BUTTON_SIZE),
        text='НАСТРОЙКИ',
        manager=manager
    )

    buttons = start_button, settings_button, inventory_button
    while True:
        time_delta = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        start_game(screen)
                    if event.ui_element == inventory_button:
                        inventory_screen(screen)
                        screen.blit(fon, (0, 0))
                        write_text(screen, intro_text, STEP_TEXT)
                    if event.ui_element == settings_button:
                        settings_screen(screen)
                        screen.blit(fon, (0, 0))
                        write_text(screen, intro_text, STEP_TEXT)
            manager.process_events(event)
        manager.update(time_delta)
        manager.update(FPS)
        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)
