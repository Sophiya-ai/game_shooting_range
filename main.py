import pygame
import random as r

pygame.init()

screen_width = 800
screen_height =600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/ba.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/i.jpg")
target_width = 50
target_height = 50
target_x = r.randint(0, screen_width - target_width)
target_y = r.randint(0, screen_height - target_height)
color = (r.randint(0,255),r.randint(0,255),r.randint(0,255))


running = True
while running:
    pass

pygame.quit()