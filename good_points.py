import random
import pygame
from main import load_image, HEIGHT, WIDTH, gamer


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
