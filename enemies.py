import random
import pygame
from main import load_image, HEIGHT, WIDTH, game_over, gamer


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