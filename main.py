import pygame
import random as r
import sys
import math

# Инициализация Pygame
pygame.init()

# Инициализация микшера
pygame.mixer.init()


# Задаем размеры и вид окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир                            !!Клавиша ПРОБЕЛ выдаст подсчет очков!!")
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

# Загрузка звуков
sound_firework = pygame.mixer.Sound('sounds/firework.wav')
sound_failed = pygame.mixer.Sound('sounds/failed.wav')
sound_shoot = pygame.mixer.Sound("sounds/shoot.wav")

# Задаем рандомную переменную цвета экрана
color = (r.randint(0,255),r.randint(0,255),r.randint(0,255))

# Устанавливаем начальные значения счётчиков
hits = 0
misses = 0

# Задаем шрифт для текста счетчика
font = pygame.font.Font(None, 36)

# Параметры фейерверка
particle_count = 100
gravity = 0.1
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]

# класс `Particle` для управления отдельными частицами фейерверка
class Particle:
    # Атрибуты:
    #`x` и `y`: Координаты частицы на экране.
    #`angle`: Угол движения частицы, случайным образом выбирается в диапазоне от 0 до \(2\pi\).
    #`speed`: Скорость частицы, случайно выбирается в диапазоне от 2 до 6.
    #`color`: Цвет частицы, случайным образом выбирается из заданного списка `colors`.
    #`radius`: Радиус частицы, установлен на 3.

    # Метод 1 - Инициализация частицы с заданными координатами `x` и `y`. Установка начальных значений для атрибутов
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = r.uniform(0, math.pi * 2)
        self.speed = r.uniform(2, 6)
        self.color = r.choice(colors)
        self.radius = 3

    # Метод 2 - Обновляет положение частицы. Положение изменяется на основе текущей скорости и угла.
    # Также учитывается сила тяжести, добавляемая к вертикальной составляющей движения.
    # Скорость постепенно уменьшается (умножается на 0.98) для моделирования трения или сопротивления воздуха.
    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle) + gravity
        self.speed *= 0.98

    # Метод 3 - Рисует частицу на заданной поверхности `s` с использованием библиотеки Pygame.
    # Частица рисуется в виде круга с заданным цветом и радиусом.
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

#Класс `Firework` управляет группой частиц и обновляет их состояние.
# Он также удаляет частицы, когда они уходят за пределы экрана
class Firework:
    # Атрибуты:
    #  `particles`: Список объектов класса`Particle`, представляющих частицы фейерверка.
    # `finished`: Логический флаг, указывающий, закончился ли фейерверк(все частицы вышли за границы экрана).
    # Метод 1 - Создает фейерверк в заданной точке `x`, `y`, инициализируя список частиц.
    def __init__(self, x, y):
        # Символ `_` используется как имя переменной цикла, чтобы показать, что его значение не используется внутри цикла:
        # когда нужно выполнить одно и то же действие несколько раз, но значения из цикла не нужны
        # Particle(x, y) - Это конструктор вызова для создания нового объекта типа `Particle` (класс выше задан)
        # Создается список self.particles из `particle_count` объектов `Particle`,
        # каждый из которых инициализируется с параметрами `x` и `y`
        self.particles = [Particle(x, y) for _ in range(particle_count)]
        self.finished = False

    # Метод 2 - Обновляет состояние всех частиц в фейерверке, вызывая их метод update
    def update(self):
        for particle in self.particles:
            particle.update()
        # Удаляем частицы, которые вышли за границы экрана. Если все частицы вышли за границы экрана
        # (например, за нижнюю границу `screen_height`), устанавливаем флаг `finished` в `True`
        self.particles = [p for p in self.particles if p.y < SCREEN_HEIGHT]
        if not self.particles:
            self.finished = True

    # Отрисовка всех частиц фейерверка на заданной поверхности
    def draw(self, s):
        for particle in self.particles:
            particle.draw(s)

# Основной игровой цикл
running = True
fireworks = []
p=0
color_text = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
while running:

    #Заливка фона
    screen.fill(color)
    #Обновляем позицию мишени
    if p==0:
        target_x += target_speed_x
        target_y += target_speed_y
        screen.blit(target_img, (target_x, target_y))
    #Проверяем столкновение с границами и меняем позицию мишени
    if (target_x == 0 or target_y == 0 or target_x + target_width > SCREEN_WIDTH
            or target_y + target_height > SCREEN_HEIGHT):
        target_x = r.randint(0, SCREEN_WIDTH - target_width)
        target_y = r.randint(0, SCREEN_HEIGHT - target_height)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Выстрел
            sound_shoot.play()
            #Определяем координаты позиции мышки и проверяем попадание
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
                target_speed_x = 0
                target_speed_y = 0
                screen.blit(target_img, (target_x, target_y))
                p = 1

    # Создаем текстовые поверхности
    if p==1:
        hits_text = font.render(f"Попадания: {hits}", True, color_text)
        misses_text = font.render(f"Промахи: {misses}", True, color_text)
        screen.blit(hits_text, (10, 10 + target_height))
        screen.blit(misses_text, (10, 50 + target_height))
        #screen.blit(target_img, (target_x, target_y))
        # Проверяем выигрыш/проигрыш
        if hits >= misses:
            sound_firework.play()
            # Создаем новый фейерверк в центре
            fireworks.append(Firework(400, 300))

    # Обновляем и рисуем фейерверки
    for firework in fireworks:
        firework.update()
        firework.draw(screen)

    # Удаляем завершенные фейерверки
    fireworks = [fw for fw in fireworks if not fw.finished]

    #Обновление окна
    pygame.display.update()
    pygame.time.delay(30)

    if hits < misses and p==1:
        sound_failed.play()
        running = False

# Цикл ожидания закрытия окна
if hits < misses and p==1:
    waiting_for_close = True
    while waiting_for_close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting_for_close = False

# Завершение Pygame
pygame.quit()

# Программа завершает свою работу и возвращает управление операционной системе
sys.exit()