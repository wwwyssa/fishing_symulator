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
fish_descriptions = [{'image_name': '1.png', 'speed': (1, -1), 'cost': (1, 10)},
                     {'image_name': '2.png', 'speed': (2, -2), 'cost': (10, 20)},
                     {'image_name': '3.png', 'speed': (3, -3), 'cost': (20, 30)},
                     {'image_name': '4.png', 'speed': (4, -4), 'cost': (30, 40)},
                     {'image_name': '5.png', 'speed': (5, -5), 'cost': (40, 50)},
                     {'image_name': '6.png', 'speed': (4, -4), 'cost': (50, 60)},
                     {'image_name': '7.png', 'speed': (3, -3), 'cost': (60, 70)},
                     {'image_name': '8.png', 'speed': (2, -2), 'cost': (70, 80)},
                     {'image_name': '9.png', 'speed': (1, -1), 'cost': (80, 100)}]

FISH_COUNT = 10
SCILL = 100

SPEED_COIL = [10, 20, 50]
ROD_PRICE = [0, 500, 10000]
EFFICIENCY = [0.25, 0.5, 0.75]

LINE_COLOR = "black"
LINE_WIDTH = 5
BEACH_BOTTOM = 65

GAME_TIME = 60

GRAVITY = 0.1
