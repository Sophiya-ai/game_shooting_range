import pygame
import random as r

# Инициализация Pygame
pygame.init()

# Задаем размеры и вид окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/ba.jpg")
pygame.display.set_icon(icon)

# Задаем параметры и вид мишени
target_img = pygame.image.load("img/i.png")
target_width = 50
target_height = 50
target_x = r.randint(0, SCREEN_WIDTH - target_width)
target_y = r.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 5
target_speed_y = 3

# Задаем рандомную переменную цвета экрана
color = (r.randint(0,255),r.randint(0,255),r.randint(0,255))

# Основной игровой цикл
running = True
while running:

    #Заливка фона
    screen.fill(color)

    #Обновляем позицию мишени
    target_x += target_speed_x
    target_y += target_speed_y

    #Проверяем столкновение с границами и меняем позицию мишени
    if (target_x == 0 or target_y == 0 or target_x + target_width > SCREEN_WIDTH
            or target_y + target_height > SCREEN_HEIGHT):
        target_x = r.randint(0, SCREEN_WIDTH - target_width)
        target_y = r.randint(0, SCREEN_HEIGHT - target_height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = r.randint(0, SCREEN_WIDTH - target_width)
                target_y = r.randint(0, SCREEN_HEIGHT - target_height)

    #Размещение мишени в окне
    screen.blit(target_img, (target_x,target_y))

    #Задержка для контроля кадров в секунду
    pygame.time.delay(30)

    #Обновление окна
    pygame.display.update()

# Завершение Pygame
pygame.quit()