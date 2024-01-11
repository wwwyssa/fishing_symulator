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

fish_fields = ["image_name", "speed", "cost"]
fish_descriptions = [{"image_name": "1.png", "speed": 5, "cost": (10, 100)}]

FISH_COUNT = 10