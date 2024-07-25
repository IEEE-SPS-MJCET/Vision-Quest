# Import
import random
import pygame
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize
pygame.init()

# Create Window/Display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Balloon Pop")

# Initialize Clock for FPS
fps = 30
clock = pygame.time.Clock()

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

# Images
imgBalloon = pygame.image.load('images/BalloonRed.png').convert_alpha()
imgStationary = pygame.image.load('images/spslogo.jpeg').convert_alpha()
new_width, new_height = 100, 100  # Desired width and height
imgStationary = pygame.transform.scale(imgStationary, (new_width, new_height))
rectBalloon = imgBalloon.get_rect()
rectBalloon.x, rectBalloon.y = 500, 300
rectStationary = imgStationary.get_rect()
rectStationary.topleft = (60, 60)

# Variables
speed = 20
score = 0
startTime = time.time()
totalTime = 30

# Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

def resetBalloon():
    rectBalloon.x = random.randint(100, width - 100)
    rectBalloon.y = height + 50

# Main loop
start = True
game_over = False

while start:
    # Get Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
            pygame.quit()

    if not game_over:
        # Apply Logic
        timeRemain = int(totalTime - (time.time() - startTime))
        if timeRemain < 0:
            game_over = True
            window.fill((255, 255, 255))

            font = pygame.font.Font(None, 50)
            textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
            textTime = font.render(f'Time UP', True, (50, 50, 255))
            textGameOver = font.render(f'Game Over', True, (255, 0, 0))
            window.blit(textScore, (450, 350))
            window.blit(textTime, (530, 275))
            window.blit(textGameOver, (500, 200))

        else:
            # OpenCV
            success, img = cap.read()
            img = cv2.flip(img, 1)
            hands, img = detector.findHands(img, flipType=False)

            rectBalloon.y -= speed  # Move the balloon up
            # Check if balloon has reached the top without pop
            if rectBalloon.y < 0:
                resetBalloon()
                speed += 1

            if hands:
                hand = hands[0]
                x, y = hand['lmList'][8][0:2]
                if rectBalloon.collidepoint(x, y):
                    resetBalloon()
                    score += 10
                    speed += 1

            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgRGB = np.rot90(imgRGB)
            frame = pygame.surfarray.make_surface(imgRGB).convert()
            frame = pygame.transform.flip(frame, True, False)
            window.blit(frame, (0, 0))
            window.blit(imgBalloon, rectBalloon)

            font = pygame.font.Font(None, 50)
            textScore = font.render(f'Score: {score}', True, (50, 50, 255))
            textTime = font.render(f'Time: {timeRemain}', True, (50, 50, 255))
            window.blit(textScore, (35, 35))
            window.blit(textTime, (1000, 35))

            # Blit the stationary image
            window.blit(imgStationary, rectStationary)

    else:
        # Display Game Over Screen
        window.fill((255, 255, 255))
        font = pygame.font.Font(None, 50)
        textScore = font.render(f'Your Score: {score}', True, (50, 50, 255))
        textTime = font.render(f'Time UP', True, (50, 50, 255))
        textGameOver = font.render(f'Game Over', True, (255, 0, 0))
        window.blit(textScore, (450, 350))
        window.blit(textTime, (530, 275))
        window.blit(textGameOver, (500, 200))
        
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()

    # Update Display
    pygame.display.update()
    # Set FPS
    clock.tick(fps)
