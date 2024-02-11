import pygame
import pygame_gui

import constants
import variables
from constants import SIZE, STEP_TEXT, BUTTON_SIZE, FPS, HEIGHT, WIDTH, INDENT, ROD_PRICE
from terminate import terminate
from util import load_image, write_text, get_button_coord


def money_upd(screen):
    font = pygame.font.Font(None, 60)
    string_rendered = font.render(f'Баланс: {variables.MONEY}', True, pygame.Color('black'))
    intro_rect = string_rendered.get_rect()
    intro_rect.top = HEIGHT / 10 * 9
    intro_rect.x = WIDTH / 2 - string_rendered.get_width() / 2
    pygame.draw.rect(screen, (135, 206, 235), (0, intro_rect.top, WIDTH, intro_rect.height))
    screen.blit(string_rendered, intro_rect)


def set_useless(i):
    if i == 0:
        variables.rod1_text = "Выбрать"
    elif i == 1:
        variables.rod2_text = "Выбрать"
    else:
        variables.rod3_text = "Выбрать"


def inventory_screen(screen):
    intro_text = ["Инвентарь"]
    text = ['1 уровень', '2 уровень', '3 уровень']
    fon = pygame.transform.scale(load_image('Sky_Blue.png'), SIZE)
    screen.blit(fon, (0, 0))
    set_manager = pygame_gui.UIManager(SIZE)
    font = pygame.font.Font(None, 30)
    write_text(screen, intro_text, STEP_TEXT)
    text_coord_y = HEIGHT / 5
    text_coord_x = WIDTH / 10
    for word in text:
        string_rendered = font.render(word, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord_y
        intro_rect.x = text_coord_x
        screen.blit(string_rendered, intro_rect)
        text_coord_x += WIDTH / 10 * 3
    money_upd(screen)
    back_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(get_button_coord(6), BUTTON_SIZE),
        text='Назад',
        manager=set_manager
    )

    rod1_but = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH / 10, HEIGHT / 5 * 3), (WIDTH / 10 * 2, HEIGHT / 20)),
        text='Выбрать',
        manager=set_manager
    )

    rod2_but = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH / 10 * 4, HEIGHT / 5 * 3), (WIDTH / 10 * 2, HEIGHT / 20)),
        text=variables.rod2_text,
        manager=set_manager
    )

    rod3_but = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((WIDTH / 10 * 7, HEIGHT / 5 * 3), (WIDTH / 10 * 2, HEIGHT / 20)),
        text=variables.rod3_text,
        manager=set_manager
    )

    frame1 = pygame.Rect(WIDTH / 10, HEIGHT / 4, WIDTH / 10 * 2, HEIGHT / 3)
    frame2 = pygame.Rect(WIDTH / 10 * 4, HEIGHT / 4, WIDTH / 10 * 2, HEIGHT / 3)
    frame3 = pygame.Rect(WIDTH / 10 * 7, HEIGHT / 4, WIDTH / 10 * 2, HEIGHT / 3)
    pygame.draw.rect(screen, 'black', frame1, 2)
    pygame.draw.rect(screen, 'black', frame2, 2)
    pygame.draw.rect(screen, 'black', frame3, 2)
    fish_rod1 = pygame.transform.scale(load_image('stick.jpg'), frame1.size)
    fish_rod2 = pygame.transform.scale(load_image('udochka.png'), frame2.size)
    fish_rod3 = pygame.transform.scale(load_image('cool_udochka.png'), frame3.size)
    screen.blit(fish_rod1, (frame1.x, frame1.y))
    screen.blit(fish_rod2, (frame2.x, frame2.y))
    screen.blit(fish_rod3, (frame3.x, frame3.y))

    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == back_button:
                        return
                    else:
                        if event.ui_element == rod1_but:
                            set_useless(variables.cur_rod)
                            variables.cur_rod = 0
                            variables.rod1_text = 'Выбрано'
                        if event.ui_element == rod2_but:
                            if 1 in variables.bought_rods:
                                set_useless(variables.cur_rod)
                                variables.cur_rod = 1
                                variables.rod2_text = 'Выбрано'
                            elif variables.MONEY >= ROD_PRICE[1]:
                                variables.MONEY -= ROD_PRICE[1]
                                variables.bought_rods.append(1)
                                variables.rod2_text = 'Выбрать'
                            money_upd(screen)
                        if event.ui_element == rod3_but:
                            if 2 in variables.bought_rods:
                                set_useless(variables.cur_rod)
                                variables.cur_rod = 2
                                variables.rod3_text = 'Выбрано'
                            elif variables.MONEY >= ROD_PRICE[2]:
                                variables.MONEY -= ROD_PRICE[2]
                                variables.rod3_text = 'Выбрать'
                                variables.bought_rods.append(2)
                            money_upd(screen)
                print(variables.MONEY)
            set_manager.process_events(event)

        rod1_but.set_text(variables.rod1_text)
        rod2_but.set_text(variables.rod2_text)
        rod3_but.set_text(variables.rod3_text)
        set_manager.update(time_delta)
        set_manager.update(FPS)
        set_manager.draw_ui(screen)
        pygame.display.flip()
        clock.tick(FPS)
