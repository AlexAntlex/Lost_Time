import pygame
from main import load_image, HEIGHT, WIDTH


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
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

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

    def shoot(self):
        now = pygame.time.get_ticks()

        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    image = load_image('bullet.png')

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Bullet.image
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.collide_mask(self, nps):
            nps.kill()
