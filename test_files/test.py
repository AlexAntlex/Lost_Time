import os
import random
import pygame
import sys

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

class Gamer(pygame.sprite.Sprite):
    gamer_image = load_image("spaceShip.png")

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Gamer.gamer_image
        self.image = pygame.transform.scale(self.image, (50, 65))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
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
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
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
        if pygame.sprite.collide_mask(self, gamer):
            game_over()


class Point(pygame.sprite.Sprite):
    point_image = load_image("star.png")

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Point.point_image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.randrange(HEIGHT)

    def update(self):
        if pygame.sprite.collide_mask(self, gamer):
            self.kill()
        if self.rect.top > HEIGHT or self.rect.right > WIDTH:
            while self.rect.top > HEIGHT or self.rect.right > WIDTH:
                self.rect.x = random.randrange(WIDTH)
                self.rect.y = random.randrange(HEIGHT)


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
        key = pygame.key.get_pressed()
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
