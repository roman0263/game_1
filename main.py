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
target_width = 80  # Исправлено опечатка в названии переменной
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)  # Исправлено опечатка в названии переменной
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Инициализация счетчиков попаданий и промахов
hits = 0
misses = 0

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1  # Увеличиваем счетчик попаданий
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                misses += 1  # Увеличиваем счетчик промахов
    screen.blit(target_img, (target_x, target_y))

    # Отрисовка счетчика внутри игрового цикла
    score_text = font.render(f'Попаданий: {hits} Промахов: {misses}', True, (255, 255, 255))
    score_pos = (10, 10)  # Позиция текста в левом верхнем углу
    screen.blit(score_text, score_pos)

    pygame.display.update()

pygame.quit()
