import pygame
import pygame_gui

from constants import SIZE, STEP_TEXT, BUTTON_SIZE, FPS, HEIGHT, WIDTH
from terminate import terminate
from util import load_image, write_text, get_button_coord


def inventory_screen(screen):
    intro_text = ["Инвентарь"]
    fon = pygame.transform.scale(load_image('Sky_Blue.png'), SIZE)
    screen.blit(fon, (0, 0))
    set_manager = pygame_gui.UIManager(SIZE)
    write_text(screen, intro_text, STEP_TEXT)
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(6), BUTTON_SIZE),
        text='Назад',
        manager=set_manager
    )
    frame1 = pygame.Rect(WIDTH / 10, HEIGHT / 4, WIDTH / 10 * 2, HEIGHT / 3)
    frame2 = pygame.Rect(WIDTH / 10 * 4, HEIGHT / 4, WIDTH / 10 * 2, HEIGHT / 3)
    frame3 = pygame.Rect(WIDTH / 10 * 7, HEIGHT / 4, WIDTH / 10 * 2, HEIGHT / 3)
    pygame.draw.rect(screen, 'black', frame1, 2)
    pygame.draw.rect(screen, 'black', frame2, 2)
    pygame.draw.rect(screen, 'black', frame3, 2)
    fish_rod1 = pygame.transform.scale(load_image('stick.jpg'), frame1.size)
    screen.blit(fish_rod1, (frame1.x, frame1.y))


    clock = pygame.Clock()
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        return
            set_manager.process_events(event)
        set_manager.update(time_delta)
        set_manager.update(FPS)
        set_manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)
