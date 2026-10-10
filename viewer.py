import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT//2

ball_rad = 25
ball_speed = 5

g = 500
Ux, Uy = 0, 0
dt = 1/60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing dot playground")

clock = pygame.time.Clock()

run = True

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Uy = -300

    screen.fill((255,255,255))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        Ux += -ball_speed*2
    if keys[pygame.K_RIGHT]:
        Ux += ball_speed*2

    ball_x += Ux*dt

    if ball_x < ball_rad:
        ball_x = ball_rad
        Ux = -Ux*0.8
    if ball_x > SCREEN_WIDTH - ball_rad:
        ball_x = SCREEN_WIDTH - ball_rad
        Ux = -Ux*0.8

    if keys[pygame.K_DOWN] and Uy > 0:
        Uy += (20/100) * Uy
    
    Uy += g*dt
    ball_y += Uy*dt  
    if ball_y >= SCREEN_HEIGHT-ball_rad:
        ball_y = SCREEN_HEIGHT-ball_rad
        Uy = -Uy * 0.8

    if ball_y <= ball_rad:
        ball_y = ball_rad
        Uy = -Uy * 0.8
    
    pygame.draw.circle(screen, (0,0,255), (ball_x, ball_y), ball_rad)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()