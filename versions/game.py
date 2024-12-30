import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

GREEN = (0, 255, 200)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Move the Square")

clock = pygame.time.Clock()

rect_width = 100
rect_height = 100
rect_x = SCREEN_WIDTH // 2 - rect_width // 2
rect_y = SCREEN_HEIGHT // 2 - rect_height // 2
rect_speed = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT] and rect_x < SCREEN_WIDTH - rect_width:
        rect_x += rect_speed
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN] and rect_y < SCREEN_HEIGHT - rect_height:
        rect_y += rect_speed

    screen.fill(GREEN)

    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

    clock.tick(144)

pygame.quit()