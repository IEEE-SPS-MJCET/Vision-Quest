import pygame
import image
from setting import *
from handTracking import HandTracking
import cv2

class Hand:
    def __init__(self):
        self.orig_image = image.load("Assests/hand.png", size=(HAND_SIZE, HAND_SIZE))
        self.image = self.orig_image.copy()
        self.image_smaller = image.load("Assests/hand.png", size=(HAND_SIZE - 50, HAND_SIZE - 50))
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, HAND_HITBOX_SIZE[0], HAND_HITBOX_SIZE[1])
        self.left_click = False

    def follow_mouse(self):
        self.rect.center = pygame.mouse.get_pos()

    def follow_mediapipe_hand(self, x, y):
        self.rect.center = (x, y)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, (200, 60, 0), self.rect)

    def draw(self, surface):
        image.draw(surface, self.image, self.rect.center, pos_mode="center")
        if DRAW_HITBOX:
            self.draw_hitbox(surface)

    def on_number(self, numbers):
        return [number for number in numbers if self.rect.colliderect(number.rect)]

    def kill_numbers(self, numbers, score, sounds):
        if self.left_click:
            for number in self.on_number(numbers):
                number_score = number.kill(numbers)
                score += number_score
                sounds["slap"].play()
                if number_score < 0:
                    sounds["screaming"].play()
        else:
            self.left_click = False
        return score
