import pygame

pygame.init()
wall_touch_count = 0  # отслеживание количества касаний стенки
W = 800  # длинна поля
H = 600  # высота поля
font = pygame.font.Font(None, 36)  # Шрифт

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption('pinball v.0.1')

# Стандартные цвета
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()

x = 0
y = H // 2 - 40
speed = 15

x1 = 780
y1 = H // 2 - 40
speed1 = 15

ball_radius = 15
ball_x = 300
ball_y = 300
ball_speed_x = 5
ball_speed_y = 5

p1_score = 0
p2_score = 0


def gameover(player):
    game_over_text = font.render(f"GAME OVER {player} LOSE", True, RED)
    game_over_rect = game_over_text.get_rect(center=(W // 2, H // 2))
    sc.blit(game_over_text, game_over_rect)
    pygame.display.update()
    pygame.time.delay(2000)
    exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        y -= speed
        if y < 0:  # Ограничение верхней границы
            y = 0
    elif keys[pygame.K_s]:
        y += speed
        if y > H - 100:  # Ограничение нижней границы
            y = H - 100

    if keys[pygame.K_UP]:
        y1 -= speed
        if y1 < 0:  # Ограничение верхней границы
            y1 = 0
    elif keys[pygame.K_DOWN]:
        y1 += speed
        if y1 > H - 100:  # Ограничение нижней границы
            y1 = H - 100

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Проверка столкновения шарика с палками
    if (ball_x - ball_radius <= x + 20 and y <= ball_y <= y + 100) or (
            ball_x + ball_radius >= x1 and y1 <= ball_y <= y1 + 100):
        ball_speed_x = -ball_speed_x
        wall_touch_count += 1

    # Проверка выхода шарика за границы экрана
    if ball_x <= ball_radius:
        p2_score += 1
        ball_speed_x = -ball_speed_x  # Изменение направления при столкновении с краем


    elif ball_x >= W - ball_radius:
        p1_score += 1
        ball_speed_x = -ball_speed_x  # Изменение направления при столкновении с краем

    if ball_y <= ball_radius or ball_y >= H - ball_radius:
        ball_speed_y = -ball_speed_y  # Изменение направления при столкновении с краем
        wall_touch_count += 1

    if wall_touch_count >= 2:
        wall_touch_count = 0  # Сбрасываем счетчик
        # Увеличиваем скорость шарика по обеим осям (можете настроить под свои потребности)
        ball_speed_x *= 1.01
        ball_speed_y *= 1.01

    sc.fill(BLACK)
    pygame.draw.line(sc, GREEN, (398, 600), (398, 0), 2)
    pygame.draw.rect(sc, BLUE, (x, y, 20, 100))
    pygame.draw.rect(sc, BLUE, (x1, y1, 20, 100))
    pygame.draw.circle(sc, YELLOW, (ball_x, ball_y), ball_radius)

    text_1_player = font.render(f"{p1_score}", True, WHITE)
    score_rect_1 = text_1_player.get_rect(center=(330, 10))  # Расположение очков 1 игрока
    sc.blit(text_1_player, score_rect_1)

    text_2_player = font.render(f"{p2_score}", True, WHITE)
    score_rect_2 = text_2_player.get_rect(center=(450, 10))  # Расположение очков 2 игрока
    sc.blit(text_2_player, score_rect_2)

    if p1_score == 10:
        gameover('Player_2')
    elif p2_score == 10:
        gameover('Player_1')

    pygame.display.update()

    clock.tick(FPS)
