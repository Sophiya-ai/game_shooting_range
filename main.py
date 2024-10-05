import pygame
import random as r
import sys

# Инициализация Pygame
pygame.init()

# Задаем размеры и вид окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир_____Клавиша ПРОБЕЛ выдаст подсчет очков!")
icon = pygame.image.load("img/ba.jpg")
pygame.display.set_icon(icon)

# Задаем параметры и вид мишени
target_img = pygame.image.load("img/i.jpg")
target_width = 50
target_height = 50
target_x = r.randint(0, SCREEN_WIDTH - target_width)
target_y = r.randint(0, SCREEN_HEIGHT - target_height)

# Задаем рандомную переменную цвета экрана
color = (r.randint(0,255),r.randint(0,255),r.randint(0,255))

# Устанавливаем начальные значения счётчиков
hits = 0
misses = 0

# Задаем шрифт для текста счетчика
font = pygame.font.Font(None, 36)

# Основной игровой цикл
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = r.randint(0, SCREEN_WIDTH - target_width)
                target_y = r.randint(0, SCREEN_HEIGHT - target_height)
                hits += 1
            else:
                target_x = r.randint(0, SCREEN_WIDTH - target_width)
                target_y = r.randint(0, SCREEN_HEIGHT - target_height)
                misses += 1

        # Обработка события нажатия клавиши Пробел
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                # Убираем мишень в угол
                target_x = 0
                target_y = 0

                # Создаем текстовые поверхности
                hits_text = font.render(f"Попадания: {hits}", True, (255, 255, 255))
                misses_text = font.render(f"Промахи: {misses}", True, (255, 255, 255))

                # Размещаем текст на экране, убираем мишень, обновляем окно и останавливаемся
                screen.blit(hits_text, (10, 10+target_height))
                screen.blit(misses_text, (10, 50+target_height))
                screen.blit(target_img, (target_x, target_y))
                pygame.display.update()
                running = False

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

# Цикл ожидания закрытия окна
waiting_for_close = True
while waiting_for_close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting_for_close = False

# Завершение Pygame
pygame.quit()

# Программа завершает свою работу и возвращает управление операционной системе
sys.exit()