import pygame

import variables
from constants import SIZE
from start_screen import start_screen

pygame.init()
screen = pygame.display.set_mode(SIZE)

start_screen(screen)

pygame.quit()
