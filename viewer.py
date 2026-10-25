import pygame, math
from physics import step_forward

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

x = 1
v = 0
scale = 150

center = SCREEN_WIDTH//2

dt = 0.05
t = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    t = t+dt

    x, v = step_forward(x, v, dt)

    screen.fill((255,255,255))

    pygame.draw.circle(screen, (0,225,0), (int(center+x*scale), SCREEN_HEIGHT//2), 15)
    pygame.draw.circle(screen, (225,0,0), (int(center+math.cos(t)*scale), SCREEN_HEIGHT//2 + 60), 15)

    print(x - math.cos(t))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()