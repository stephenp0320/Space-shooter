import pygame
import random

# General setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Image imports
player_surf = pygame.image.load("../images/player.png")
big_rock = pygame.image.load("../images/meteorBig.png")
small_rock = pygame.image.load("../images/meteorSmall.png")
big_star = pygame.image.load("../images/starBig.png")
small_star = pygame.image.load("../images/starSmall.png")

num_stars = 100
stars = []

for i in range(num_stars):
    star = {
        'surf': random.choice([big_star, small_star]),
        'x': random.randint(0, screen.get_width()),
        'y': random.randint(0, screen.get_width())
    }
    stars.append(star)
# Rock attributes
num_rocks = 5  # Number of rocks
space_rocks = []

for i in range(num_rocks):
    rock = {
        'surf': random.choice([big_rock, small_rock]),  # Randomly choose between big and small rocks
        'x': random.randint(0, screen.get_width()),
        'y': random.randint(-screen.get_height(), 0),  # Start off-screen
        'speed_x': random.randint(1, 5),  # Random horizontal speed
        'speed_y': random.randint(1, 7)  # Random vertical speed
    }
    space_rocks.append(rock)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_x, mouse_y = pygame.mouse.get_pos()  # Update mouse position

    screen.fill("black")
    for star in stars:
        screen.blit(star['surf'], (star['x'], star['y']))

    for rock in space_rocks:
        # Update rock position
        rock['x'] += rock['speed_x']
        rock['y'] += rock['speed_y']

        # If the rock moves off the screen, reset its position
        if rock['x'] > screen.get_width():
            rock['x'] = -rock['surf'].get_width()
        if rock['y'] > screen.get_height():
            rock['y'] = -rock['surf'].get_height()

        # Draw the rock
        screen.blit(rock['surf'], (rock['x'], rock['y']))

    screen.blit(player_surf, (mouse_x, mouse_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
