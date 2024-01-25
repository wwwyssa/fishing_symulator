import sys
import pygame

from variables import save_progress


def terminate():
    save_progress()
    pygame.quit()
    sys.exit()
