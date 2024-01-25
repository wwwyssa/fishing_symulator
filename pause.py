import pygame
import pygame_gui

from constants import FPS, STEP_TEXT, SIZE, BUTTON_SIZE, HEIGHT, WIDTH
from terminate import terminate
from util import write_text, get_button_coord


def pause(screen):
    font = pygame.font.Font(None, 80)
    string_rendered = font.render('ПАУЗА ', 1, pygame.Color('black'))
    text = string_rendered.get_rect()
    text.top = HEIGHT / 8 * 3
    text.x = WIDTH // 2 - text.width // 2 + 10
    frame1 = pygame.Rect(WIDTH // 2 - text.width, HEIGHT // 8 * 3, text.width * 2, HEIGHT / 3)
    pygame.draw.rect(screen, 'lightblue', frame1)
    pygame.draw.rect(screen, 'black', frame1, width=3)
    screen.blit(string_rendered, text)

    manager = pygame_gui.UIManager(SIZE)
    clock = pygame.time.Clock()

    continue_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(4), BUTTON_SIZE),
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
                        pygame.mouse.set_visible(False)
                        return 1
                    if event.ui_element == back_button:
                        return 0
            manager.process_events(event)
        manager.update(time_delta)
        manager.update(FPS)
        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)
