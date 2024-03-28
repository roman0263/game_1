import pygame
import random
import sys

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
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

game_duration = 120  # Игра длится 2 минуты

# Начальные значения
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = 0.1
target_speed_y = 0.1
hits = 0
misses = 0
is_paused = False
start_ticks = pygame.time.get_ticks()  # Запоминаем время старта

running = True
while running:
    current_ticks = pygame.time.get_ticks()
    elapsed_time = (current_ticks - start_ticks) // 1000  # Время с начала игры в секундах
    remaining_time = max(game_duration - elapsed_time, 0)  # Оставшееся время

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                is_paused = not is_paused
        if not is_paused and event.type == pygame.MOUSEBUTTONDOWN:
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

    if not is_paused and remaining_time > 0:
        target_x += target_speed_x
        target_y += target_speed_y
        if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
            target_speed_x = -target_speed_x
        if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
            target_speed_y = -target_speed_y
    else:
        # Останавливаем игру, если время вышло
        game_over_text = font.render('Время вышло! Нажмите любую клавишу для выхода.', True, (255, 255, 255))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

    screen.fill(color)
    screen.blit(target_img, (target_x, target_y))
    score_text = font.render(f'Попаданий: {hits} Промахов: {misses}', True, (255, 255, 255))
    time_text = font.render(f'Оставшееся время: {remaining_time // 60}:{remaining_time % 60:02d}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 40))

    if is_paused:
        pause_text = font.render('Пауза', True, (255, 255, 255))
        screen.blit(pause_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))

    pygame.display.update()

pygame.quit()
