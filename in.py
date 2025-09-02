import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("역학적 에너지 보존")


LIKE = (20, 255, 100)
WHITE = (255, 255, 255)
RED = (100,200,10)
player_start_size = 22
player_y = player_start_size
player_x = WIDTH / 2 - player_start_size / 2
player_v = 0
G = 9.8

floor_y = HEIGHT - player_start_size



clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (player_x, player_y), player_start_size)
    pygame.draw.rect(screen, LIKE, (0, floor_y, WIDTH, player_start_size))  # 바닥

    player_position_power = (G * (floor_y - player_start_size - player_y ))
    player_exercise_power = (1/2 * player_v ** 2 )
    player_physic_power = player_position_power + player_exercise_power

    
    
    font = pygame.font.SysFont("consolas", 24)
    text2_surface = font.render(str(player_position_power), True, (100, 100, 255))
    text_surface = font.render(str(player_exercise_power), True, (100, 100, 255))
    text3_surface = font.render(str(player_physic_power), True, (100, 100, 255))
    screen.blit(text_surface, (0, 0))
    screen.blit(text2_surface, (0, 25))
    screen.blit(text3_surface, (0, 50))
    
    se = clock.tick(120) / 1000.0
    player_v += se * G
    player_y += player_v * se



    if player_y <= floor_y - player_start_size:
        pygame.display.flip()

    
    clock.tick(240)

pygame.quit()
sys.exit()
