import pygame
import pygame_gui

from constants import SIZE, STEP_TEXT
from util import load_image, write_text


def settings_screen(screen):
    intro_text = ["Настройки"]
    fon = pygame.transform.scale(load_image('light_purple.png'), SIZE)
    screen.blit(fon, (0, 0))
    write_text(screen, intro_text, STEP_TEXT)
