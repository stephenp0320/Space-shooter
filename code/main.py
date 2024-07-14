import pygame
import random
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../images/player.png")
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.lasers = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        player_direction_x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        player_direction_y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        # Update player position
        self.rect.x += player_direction_x * 5
        self.rect.y += player_direction_y * 5

        # Ensure the player stays within the screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

        # Fire laser with space key
        if keys[pygame.K_SPACE]:
            self.fire_laser()

        # Update lasers
        self.lasers.update()

    def fire_laser(self):
        laser = Laser(self.rect.centerx, self.rect.top, self.lasers)
        self.lasers.add(laser)
        all_sprites.add(laser)


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y, groups):
        super().__init__(groups)
        self.image = pygame.image.load("../images/laserRed.png")
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

class Rock(pygame.sprite.Sprite):
    def __init__(self, image, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(
            center=(random.randint(0, WINDOW_WIDTH), random.randint(-WINDOW_HEIGHT, 0))
        )
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1, 7)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Reset position if the rock moves off the screen
        if self.rect.x > WINDOW_WIDTH:
            self.rect.x = -self.rect.width
        if self.rect.y > WINDOW_HEIGHT:
            self.rect.y = -self.rect.height

# General setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
pygame.mixer.music.load("../audio/n-Dimensions (Main Theme).mp3")

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
player = Player(all_sprites)

# Image imports
big_rock_img = pygame.image.load("../images/meteorBig.png")
small_rock_img = pygame.image.load("../images/meteorSmall.png")
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
num_rocks = 15  # Number of rocks

for i in range(num_rocks):
    image = random.choice([big_rock_img, small_rock_img])
    Rock(image, [all_sprites, rocks])

pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Check for collisions between lasers and rocks
    collisions = pygame.sprite.groupcollide(player.lasers, rocks, True, True)
    if collisions:
        print("Rock exploded!")

    # Check for collisions between player and rocks
    if pygame.sprite.spritecollide(player, rocks, False):
        print("Collision detected!")
        running = False  # End the game on collision

    screen.fill("black")

    # Draw the stars
    for star in stars:
        screen.blit(star['surf'], (star['x'], star['y']))

    # Draw all sprites
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
