import pygame
import pygame_gui

from constants import WIDTH, HEIGHT, FPS, STEP_TEXT, INDENT, SIZE, fon_sound, BUTTON_WIDTH, BUTTON_HEIGHT
from game_screen import start_game
from inventory_screen import inventory_screen
from settings_screen import settings_screen
from terminate import terminate
from util import load_image




def start_screen(screen):
    intro_text = ["Рыбалка"]
    fon_sound.set_volume(0.5)
    fon_sound.play()
    fon = pygame.transform.scale(load_image('start_fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 60)
    text_coord = INDENT
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = (WIDTH - intro_rect.width) // 2
        text_coord += intro_rect.height + STEP_TEXT
        screen.blit(string_rendered, intro_rect)

    manager = pygame_gui.UIManager(SIZE)
    clock = pygame.time.Clock()

    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT / 8 * 3), (BUTTON_WIDTH, BUTTON_HEIGHT)),
        text='СТАРТ',
        manager=manager
    )

    inventory_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT / 8 * 4), (BUTTON_WIDTH, BUTTON_HEIGHT)),
        text='ИНВЕНТАРЬ',
        manager=manager

    )

    settings_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT / 8 * 5), (BUTTON_WIDTH, BUTTON_HEIGHT)),
        text='НАСТРОЙКИ',
        manager=manager
    )
    buttons = start_button, settings_button, inventory_button
    while True:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        start_game(screen)
                    if event.ui_element == inventory_button:
                        inventory_screen(screen)
                    if event.ui_element == settings_button:
                        settings_screen(screen)
                    for button in buttons:
                        button.hide()
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)
