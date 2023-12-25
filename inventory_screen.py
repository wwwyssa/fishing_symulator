import pygame
import pygame_gui

from constants import WIDTH, HEIGHT, FPS, STEP_TEXT, INDENT, SIZE
from terminate import terminate
from util import load_image

def inventory_screen(screen):
    intro_text = ["Инвентарь"]
    fon = pygame.transform.scale(load_image('Sky_Blue.png'), (WIDTH, HEIGHT))
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


