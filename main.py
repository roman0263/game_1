import pygame
import random

pygame.init()
pygame.font.init()  # Инициализация модуля шрифтов Pygame
font_size = 24
font = pygame.font.Font(None, font_size)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("imge/strelkovy_stol.jpg")
pygame.display.set_icon(icon)
target_img = pygame.image.load("imge/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 0.1
target_speed_y = 0.1
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

hits = 0
misses = 0
is_paused = False  # Переменная для отслеживания состояния паузы

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Проверка нажатия клавиш
            if event.key == pygame.K_p:  # Нажата клавиша P
                is_paused = not is_paused  # Переключение состояния паузы
        if not is_paused:  # Обработка событий только если игра не на паузе
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                    hits += 1
                    if hits % 5 == 0:
                        target_speed_x += 0.1 if target_speed_x > 0 else -0.1
                        target_speed_y += 0.1 if target_speed_y > 0 else -0.1
                    target_x = random.randint(0, SCREEN_WIDTH - target_width)
                    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                else:
                    misses += 1

    screen.fill(color)
    if not is_paused:  # Движение и обновление игры только если не на паузе
        target_x += target_speed_x
        target_y += target_speed_y
        if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
            target_speed_x = -target_speed_x
        if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
            target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))
    score_text = font.render(f'Попаданий: {hits} Промахов: {misses}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    if is_paused:
        pause_text = font.render('Пауза', True, (255, 255, 255))
        screen.blit(pause_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))

    pygame.display.update()

pygame.quit()
