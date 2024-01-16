import pygame

pygame.init()

SIZE = (WIDTH, HEIGHT) = (900, 700)
SCREEN_RECT = (0, 0, *SIZE)
FPS = 50

BUTTON_SIZE = BUTTON_WIDTH, BUTTON_HEIGHT = (250, 50)

MUSIC_VOLUME = 0.5
fon_sound = pygame.mixer.Sound('data/fon_mus.mp3')
INDENT = 50
STEP_TEXT = 10

FISH_SIZE = (150, 85)
fish_fields = ["image_name", "speed", "cost"]
fish_descriptions = [{'image_name': '1.png', 'speed': (1, -1), 'cost': (10, 100)},
                     {'image_name': '2.png', 'speed': (2, -2), 'cost': (10, 100)},
                     {'image_name': '3.png', 'speed': (3, -3), 'cost': (10, 100)},
                     {'image_name': '4.png', 'speed': (4, -4), 'cost': (10, 100)},
                     {'image_name': '5.png', 'speed': (5, -5), 'cost': (10, 100)},
                     {'image_name': '6.png', 'speed': (6, -6), 'cost': (10, 100)},
                     {'image_name': '7.png', 'speed': (7, -7), 'cost': (10, 100)},
                     {'image_name': '8.png', 'speed': (8, -8), 'cost': (10, 100)},
                     {'image_name': '9.png', 'speed': (9, -9), 'cost': (10, 100)}]

FISH_COUNT = 5