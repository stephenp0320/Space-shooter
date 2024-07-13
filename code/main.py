import pygame
import math

# General setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
surf = pygame.Surface((100, 200))
x = 100

# Image imports
player_surf = pygame.image.load("../images/player.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()  # Update mouse position

    screen.fill("darkgrey")
    screen.blit(surf, (x, 150))
    screen.blit(player_surf, (mouse_x, mouse_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
