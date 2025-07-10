import pygame
import random
from src import Player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
player = Player.Player()
running = True
dt = 0
Score = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


def ground():
    pygame.draw.rect(screen, "darkgreen", (0, 650, 1280, 1280))


def platform(posx, posy):
    return pygame.Rect(posy, posx, 100, 30)
        

def gravity(pos):
    if player_pos.y <= pos:
        player_pos.y += 500 * dt


def outOfBounce():
    if player_pos.x >= 1280:
        player_pos.x = 1
    if player_pos.x <= 0:
        player_pos.x = 1279


platforms = [platform(
    random.uniform(100, 500),
    random.uniform(100, 500)
) for _ in range(3)]



while running:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


    screen.fill("lightblue")

    circle = player.shape(screen, player_pos)
    ground()
    #gravity(610)
    outOfBounce()


    #platform1 = platform(300, 200, "black")
    #platform(200, 300, "grey")


    for p in platforms:
        if p.colliderect(circle):
            gravity(p[1]-40)
            break 
    else:
        gravity(610)





    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player_pos.y -= 1000 * dt
    if keys [pygame.K_a]:
        player_pos.x -= 1000 * dt
    if keys [pygame.K_d]:
        player_pos.x += 1000 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()