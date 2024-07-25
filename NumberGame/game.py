import pygame
import time
import random
from setting import *
from background import Background
from hand import Hand
from handTracking import HandTracking
from numbergame import PositiveNumber, NegativeNumber
import cv2
import ui

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.cap = cv2.VideoCapture(0)

        self.sounds = {}
        self.sounds["slap"] = pygame.mixer.Sound(f"Assests\sound\collect-points-190037.mp3")
        self.sounds["slap"].set_volume(SOUNDS_VOLUME)
        self.sounds["screaming"] = pygame.mixer.Sound(f"Assests/Sound/screaming.wav")
        self.sounds["screaming"].set_volume(SOUNDS_VOLUME)

    def reset(self):
        self.hand_tracking = HandTracking()
        self.hand = Hand()
        self.numbers = []
        self.spawn_timer = 0
        self.score = 0
        self.game_start_time = time.time()
        self.time_left = GAME_DURATION
        self.game_over = False

    def spawn_numbers(self):
        t = time.time()
        if t > self.spawn_timer:
            self.spawn_timer = t + SPAWN_TIME

            if random.randint(0, 100) < 50:
                self.numbers.append(PositiveNumber())
            else:
                self.numbers.append(NegativeNumber())

    def load_camera(self):
        _, self.frame = self.cap.read()

    def set_hand_position(self):
        self.frame = self.hand_tracking.scan_hands(self.frame)
        (x, y) = self.hand_tracking.get_hand_center()
        self.hand.rect.center = (x, y)

    def draw(self):
        self.background.draw(self.surface)
        for number in self.numbers:
            number.draw(self.surface)
        self.hand.draw(self.surface)
        ui.draw_text(self.surface, f"Score : {self.score}", (5, 5), COLORS["score"], font=FONTS["medium"],
                     shadow=True, shadow_color=(255, 255, 255))
        timer_text_color = (160, 40, 0) if self.time_left < 5 else COLORS["timer"]
        ui.draw_text(self.surface, f"Time left : {self.time_left}", (SCREEN_WIDTH//2, 5), timer_text_color, font=FONTS["medium"],
                     shadow=True, shadow_color=(255, 255, 255))

        # Display the target score
        ui.draw_text(self.surface, f"Target : {TARGET_SCORE}", (SCREEN_WIDTH - 150, 5), COLORS["target"], font=FONTS["medium"],
                     shadow=True, shadow_color=(255, 255, 255))

        if self.game_over:
            ui.display_winner_message(self.surface)  # Show winner message

    def game_time_update(self):
        if not self.game_over:  # Only update time if game is not over
            self.time_left = max(round(GAME_DURATION - (time.time() - self.game_start_time), 1), 0)

    def check_win_condition(self):
        if self.score >= TARGET_SCORE:
            self.game_over = True

    def update(self):
        self.load_camera()
        self.set_hand_position()
        self.game_time_update()
        self.draw()

        if self.time_left > 0 and not self.game_over:
            self.spawn_numbers()
            (x, y) = self.hand_tracking.get_hand_center()
            self.hand.rect.center = (x, y)
            self.hand.left_click = self.hand_tracking.hand_closed
            if self.hand.left_click:
                self.hand.image = self.hand.image_smaller.copy()
            else:
                self.hand.image = self.hand.orig_image.copy()
            self.score = self.hand.kill_numbers(self.numbers, self.score, self.sounds)
            for number in self.numbers:
                number.move()

            self.check_win_condition()

        if self.time_left <= 0 or self.game_over:
            if ui.button(self.surface, 540, "Continue", click_sound=self.sounds["slap"]):
                return "menu"

        cv2.imshow("Frame", self.frame)
        cv2.waitKey(1)
