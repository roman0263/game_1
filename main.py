import pygame
import random

pygame.init()
pygame.font.init()
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

def reset_game():
    global target_x, target_y, target_speed_x, target_speed_y, hits, misses, start_ticks, is_paused
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    # Уменьшаем начальную скорость мишени
    target_speed_x = random.uniform(-0.1, 1.5)
    target_speed_y = random.uniform(-0.1, 1.5)
    hits = 0
    misses = 0
    start_ticks = pygame.time.get_ticks()
    is_paused = False

reset_game()

game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not game_over:
                is_paused = not is_paused
            elif event.key == pygame.K_r and game_over:
                reset_game()
                game_over = False

    if not is_paused and not game_over:
        current_ticks = pygame.time.get_ticks()
        elapsed_time = (current_ticks - start_ticks) // 1000

        if elapsed_time >= 300 or hits >= 100:
            game_over = True

    screen.fill(color)
    if not is_paused and not game_over:
        if pygame.mouse.get_pressed()[0]:  # Проверяем нажатие левой кнопки мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                hits += 1
                if hits % 5 == 0:
                    # Постепенно увеличиваем скорость после каждых 5 попаданий
                    target_speed_x += 0.1 if target_speed_x > 0 else -0.1
                    target_speed_y += 0.1 if target_speed_y > 0 else -0.1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                misses += 1

        target_x += target_speed_x
        target_y += target_speed_y
        if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width or target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
            target_speed_x = -target_speed_x
            target_speed_y = -target_speed_y

    screen.blit(target_img, (target_x, target_y))
    score_text = font.render(f'Попаданий: {hits} Промахов: {misses}', True, (255, 255, 255))
    time_text = font.render(f'Время: {elapsed_time // 60}:{elapsed_time % 60:02d} мин', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(time_text, (10, 40))

    if is_paused:
        pause_text = font.render('Пауза', True, (255, 255, 255))
        screen.blit(pause_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2))
    if game_over:
        game_over_text = font.render('Игра окончена! Нажмите R для рестарта', True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2))

    pygame.display.update()

pygame.quit()
