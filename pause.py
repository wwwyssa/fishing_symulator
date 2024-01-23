import pygame
import pygame_gui

from constants import FPS, STEP_TEXT, SIZE, BUTTON_SIZE
from terminate import terminate
from util import write_text, get_button_coord


def pause(screen):
    pygame.mouse.set_visible(True)
    intro_text = ["ПАУЗА"]

    write_text(screen, intro_text, STEP_TEXT)

    manager = pygame_gui.UIManager(SIZE)
    clock = pygame.time.Clock()

    continue_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(3), BUTTON_SIZE),
        text='Продолжить',
        manager=manager
    )

    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(5), BUTTON_SIZE),
        text='На главный экран',
        manager=manager

    )

    while True:
        time_delta = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == continue_button:
                        return 1
                    if event.ui_element == back_button:
                        return 0
            manager.process_events(event)
        manager.update(time_delta)
        manager.update(FPS)
        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)
