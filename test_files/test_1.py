import os
import random

import pygame
import sys

pygame.init()
WIDTH = 600
HEIGHT = 600
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


class GamerCar(pygame.sprite.Sprite):
    gamer_image = load_image("car.png")

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = GamerCar.gamer_image
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.speedx = -8
        if key[pygame.K_RIGHT]:
            self.speedx = 8
        if key[pygame.K_UP]:
            self.speedy = -8
        if key[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


class NPS(pygame.sprite.Sprite):
    NPS_image = load_image("nps.png")

    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = NPS.NPS_image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    pass


background = pygame.transform.scale(load_image('fon.png'), (WIDTH, HEIGHT))
background_rect = background.get_rect()
clock = pygame.time.Clock()
fps = 60


gamer_sprite = pygame.sprite.Group()
gamer = GamerCar()
gamer_sprite.add(gamer)

NPS_sprites = pygame.sprite.Group()
for _ in range(7):
    NPS(NPS_sprites)

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
    gamer_sprite.update()
    screen.fill((0, 0, 0))
    screen.blit(background, background_rect)
    gamer_sprite.draw(screen)
    NPS_sprites.draw(screen)
    NPS_sprites.update()
    pygame.display.flip()