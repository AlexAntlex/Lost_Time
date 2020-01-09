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