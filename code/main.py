import pygame
import random
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../images/player.png")
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.mixer.music.load("../audio/n-Dimensions (Main Theme).mp3")

player = Player()

# Image imports
# player_surf = pygame.image.load("../images/player.png")
# player_rect = player_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
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
        'y': random.randint(0, screen.get_height())  # Corrected to use screen height
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

pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # THE MOVEMENT FOR THE SPACESHIP
    # keys = pygame.key.get_pressed()
    # player_direction_x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # player_direction_y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    # # Update player position
    # player_rect.x += player_direction_x * 5
    # player_rect.y += player_direction_y * 5
    #
    # # Ensure the player stays within the screen bounds
    # if player_rect.left < 0:
    #     player_rect.left = 0
    # if player_rect.right > WINDOW_WIDTH:
    #     player_rect.right = WINDOW_WIDTH
    # if player_rect.top < 0:
    #     player_rect.top = 0
    # if player_rect.bottom > WINDOW_HEIGHT:
    #     player_rect.bottom = WINDOW_HEIGHT

    screen.fill("black")

    # Draw the stars
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

    # Draw the player ship
   # screen.blit(player_surf, player_rect.topleft)
    screen.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
