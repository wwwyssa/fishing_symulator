import pygame
import pygame_gui

from constants import WIDTH, HEIGHT, FPS, STEP_TEXT, INDENT, SIZE, fon_sound
from constants import BUTTON_WIDTH, BUTTON_HEIGHT
from terminate import terminate
from util import load_image

def settings_screen(screen):
    intro_text = ["Настройки"]
    fon = pygame.transform.scale(load_image('light_purple.png'), (WIDTH, HEIGHT))
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
    pygame.display.flip()
    running = True
    manager = pygame_gui.UIManager(SIZE)
    music_volume_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT / 8 * 2), (BUTTON_WIDTH, BUTTON_HEIGHT)),
        manager=manager,
        start_value = 50,
        value_range= (0, 100)
    )


    clock = pygame.Clock()
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    fon_sound.set_volume(music_volume_slider.current_value / 100)
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)

