import os
import pygame
import sys
from gamer_car import GamerCar
from NPS_car import NPS

pygame.init()
WIDTH = 600
HEIGHT = 600
size = WIDTH, HEIGHT
screen = pygame.display.set_mode(size)


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


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