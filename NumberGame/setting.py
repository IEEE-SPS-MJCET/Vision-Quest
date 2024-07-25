import pygame
WINDOW_NAME = "Cockroach Exterminator"
GAME_TITLE = WINDOW_NAME
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
HAND_SIZE = 100
FPS = 90
DRAW_FPS = True
HAND_HITBOX_SIZE = (80, 80)
MOVE_SPEED = {"min": 3, "max": 5}
SPAWN_TIME = 0.5
BUTTONS_SIZES = (240, 90)
GAME_DURATION = 60  # seconds
SOUNDS_VOLUME = 0.3
DRAW_HITBOX = False
TARGET_SCORE = 20  # Set the target score to win the game

# sounds / music
MUSIC_VOLUME = 0.16 # value between 0 and 1
SOUNDS_VOLUME = 1

COLORS = {
    "score": (255, 255, 0),
    "timer": (0, 255, 0),
    "target": (0, 0, 255)
}


import pygame

WINDOW_NAME = "NUMBER GAME"
GAME_TITLE = WINDOW_NAME

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

FPS = 90
DRAW_FPS = True


# drawing
DRAW_HITBOX = False # will draw all the hitbox

# animation
ANIMATION_SPEED = 0.05 # the frame of the insects will change every X sec

# difficulty
GAME_DURATION = 30 # the game will last X sec

# colors
COLORS = {"title": (0, 255, 255), "score": (255, 0, 0), "timer": (0, 0, 0),
            "buttons": {"default": (56, 67, 209), "second":  (87, 99, 255),
                        "text": (255, 255, 255), "shadow": (46, 54, 163)},
            "target": (0, 0, 255)} # second is the color when the mouse is on the button

# sounds / music
MUSIC_VOLUME = 0.16 # value between 0 and 1
SOUNDS_VOLUME = 1

# fonts
pygame.font.init()

FONTS = {
    "medium": pygame.font.Font(None, 36),  # Example font size
    "large": pygame.font.Font(None, 72),
    "big": pygame.font.Font(None, 120)
}

