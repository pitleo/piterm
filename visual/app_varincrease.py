import pygame
import time
def playNotificationSount():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("default.wav")
    pygame.mixer.music.play()
    time.sleep(10)
playNotificationSount()