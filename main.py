import pygame
import random as r

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/ba.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/i.jpg")
target_width = 50
target_height = 50
target_x = r.randint(0, SCREEN_WIDTH - target_width)
target_y = r.randint(0, SCREEN_HEIGHT - target_height)
color = (r.randint(0,255),r.randint(0,255),r.randint(0,255))

running = True
while running:
    pass

pygame.quit()