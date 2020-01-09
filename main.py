import os
import pygame
import sys
from gamer import Gamer
from enemies import NPS
from good_points import Point


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
area = screen.get_rect()
WIDTH = area[2]
HEIGHT = area[3]

counter, text = 3, '3'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('agencyfb', 62)
stop = False


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


background = pygame.transform.scale(load_image('farback.png'), (WIDTH, HEIGHT))
background_rect = background.get_rect()
clock = pygame.time.Clock()
fps = 60


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    pass


def pause():
    global stop
    font = pygame.font.SysFont('agencyfb', 62)
    text = 'pause'
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        stop = False
        screen.blit(font.render(text, True, (255, 255, 255)), (WIDTH / 2.1, HEIGHT / 2.2))
        pygame.display.update()
        clock.tick(fps)


def options():
    pass


def game_over():
    font = pygame.font.SysFont('agencyfb', 62)
    text = 'Game Over'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        screen.blit(font.render(text, True, (255, 255, 255)), (WIDTH / 2.5, HEIGHT / 2.2))
        pygame.display.update()
        clock.tick(fps)


gamer_sprite = pygame.sprite.Group()
gamer = Gamer()
gamer_sprite.add(gamer)

NPS_sprites = pygame.sprite.Group()
for _ in range(7):
    NPS(NPS_sprites)

point_sprites = pygame.sprite.Group()
for _ in range(3):
    star = Point()
    point_sprites.add(star)


while True:
    clock.tick(fps)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                    stop = True
                    pause()
        if event.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
    if counter > 0:
        screen.fill((0, 0, 0))
        screen.blit(background, background_rect)
        gamer_sprite.draw(screen)
        screen.blit(font.render(text, True, (255, 255, 255)), (WIDTH / 2.1, HEIGHT / 2.2))
        pygame.display.flip()
    elif counter <= 0:
        gamer_sprite.update()
        screen.fill((0, 0, 0))
        screen.blit(background, background_rect)
        gamer_sprite.draw(screen)
        NPS_sprites.draw(screen)
        point_sprites.draw(screen)
        point_sprites.update()
        NPS_sprites.update()
        pygame.display.flip()
