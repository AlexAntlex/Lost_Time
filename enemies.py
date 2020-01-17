import random
import pygame
from had_files import WIDTH, HEIGHT, game_over, explosion_anim
from load_files import load_image


class NPS(pygame.sprite.Sprite):
    enemies_ships = [load_image('nps_1.png'),
                     load_image('nps_2.png'),
                     load_image('nps_3.png')]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(NPS.enemies_ships)
        self.image = pygame.transform.scale(self.image, (50, 60))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.radius = int(self.rect.width * 0.85 / 2)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self, gamer=None, score=0):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        if pygame.sprite.collide_mask(self, gamer):
            game_over(score)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size, explosion_anim):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
