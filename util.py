import os
import sys
import pygame

from constants import INDENT, WIDTH, BUTTON_WIDTH, HEIGHT


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    print(fullname, name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((10, 10))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def write_text(screen, intro_text, step_text):
    font = pygame.font.Font(None, 60)
    text_coord = INDENT
    for line in intro_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = text_coord
        intro_rect.x = get_center_coord_x(intro_rect.width)
        text_coord += intro_rect.height + step_text
        screen.blit(string_rendered, intro_rect)


def get_center_coord_x(width):
    return (WIDTH - width) // 2


def get_button_coord(ind):
    return get_center_coord_x(BUTTON_WIDTH), HEIGHT // 8 * ind
