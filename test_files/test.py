import os
import random
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
area = screen.get_rect()
WIDTH = area[2]
HEIGHT = area[3]

pygame.time.set_timer(pygame.USEREVENT, 1000)


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


background = pygame.transform.scale(load_image('farback.png'), (WIDTH, HEIGHT))
background_rect = background.get_rect()
clock = pygame.time.Clock()
fps = 60

bullets = pygame.sprite.Group()

explosion_anim = {}
explosion_anim['lg'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = load_image(filename)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)


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


class NPS(pygame.sprite.Sprite):
    NPS_image = load_image("nps.png")

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
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


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
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


class GameIcon(pygame.sprite.Sprite):
    icons = [load_image('Sun_00000.png'),
             load_image('Sun_00001.png'),
             load_image('Sun_00002.png'),
             load_image('Sun_00003.png'),
             load_image('Sun_00004.png'),
             load_image('Sun_00005.png'),
             load_image('Sun_00006.png'),
             load_image('Sun_00007.png'),
             load_image('Sun_00008.png'),
             load_image('Sun_00009.png'),
             load_image('Sun_00010.png'),
             load_image('Sun_00011.png'),
             load_image('Sun_00012.png'),
             load_image('Sun_00013.png'),
             load_image('Sun_00014.png')]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = GameIcon.icons[0]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2.5
        self.rect.y = HEIGHT / 2.2 - 60
        self.count = 0

    def update(self):
        self.count += 1
        if self.count > 14:
            self.count = 0
        self.image = GameIcon.icons[self.count]


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    pass


def pause():
    global stop
    font = pygame.font.SysFont('agencyfb', 80)
    font_2 = pygame.font.SysFont('agencyfb', 50)
    text = 'pause'
    text_2 = 'Press M to return to the menu.'
    text_3 = 'Press R to restart'
    text_4 = 'Press BACKSPACE to exit the game.'
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop = False
                if event.key == pygame.K_m:
                    start_screen()
                if event.key == pygame.K_BACKSPACE:
                    terminate()
        screen.fill((0, 0, 0))
        screen.blit(background, background_rect)
        gamer_sprite.draw(screen)
        NPS_sprites.draw(screen)
        point_sprites.draw(screen)
        icon_sprite.draw(screen)
        icon_sprite.update()
        screen.blit(font.render(text, True, (47, 41, 56)), (WIDTH / 2.1, HEIGHT / 2.2 - 60))
        screen.blit(font_2.render(text_2, True, (255, 255, 255)), (WIDTH / 3, HEIGHT / 2.2 + 60))
        screen.blit(font_2.render(text_3, True, (255, 255, 255)), (WIDTH / 3, HEIGHT / 2.2 + 120))
        screen.blit(font_2.render(text_4, True, (255, 255, 255)), (WIDTH / 3, HEIGHT / 2.2 + 180))
        pygame.display.update()
        clock.tick(15)


def game_over():
    font = pygame.font.SysFont('agencyfb', 50)
    font_2 = pygame.font.SysFont('agencyfb', 80)
    text_1 = 'Game Over'
    text_2 = 'Press M to return to the menu.'
    text_3 = 'Press R to restart'
    text_4 = 'Press BACKSPACE to exit the game.'
    while True:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or key[pygame.K_BACKSPACE]:
                terminate()
            if key[pygame.K_m]:
                start_screen()
            if key[pygame.K_r]:
                pass
        screen.fill((0, 0, 0))
        screen.blit(background, background_rect)
        gamer_sprite.draw(screen)
        NPS_sprites.draw(screen)
        point_sprites.draw(screen)
        icon_sprite.draw(screen)
        icon_sprite.update()
        screen.blit(font_2.render(text_1, True, (47, 41, 56)), (WIDTH / 2.5, HEIGHT / 2.2 - 30))
        screen.blit(font.render(text_2, True, (255, 255, 255)), (WIDTH / 2, HEIGHT / 2.2 + 60))
        screen.blit(font.render(text_3, True, (255, 255, 255)), (WIDTH / 2, HEIGHT / 2.2 + 120))
        screen.blit(font.render(text_4, True, (255, 255, 255)), (WIDTH / 2, HEIGHT / 2.2 + 180))
        pygame.display.update()
        clock.tick(15)


gamer_sprite = pygame.sprite.Group()
gamer = Gamer()
gamer_sprite.add(gamer)

NPS_sprites = pygame.sprite.Group()
for _ in range(7):
    nps = NPS()
    NPS_sprites.add(nps)

point_sprites = pygame.sprite.Group()
for _ in range(3):
    star = Point()
    point_sprites.add(star)

icon_sprite = pygame.sprite.Group()
icon = GameIcon()
icon_sprite.add(icon)

counter, text = 4, '3'.rjust(3)
time_stars = 0

eploude_sprite = pygame.sprite.Group()

while True:
    time_stars += 1
    font = pygame.font.SysFont('agencyfb', 62)
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                    stop = True
                    pause()
            if event.key == pygame.K_SPACE:
                gamer.shoot()
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
        bullets.draw(screen)
        gamer_sprite.draw(screen)
        NPS_sprites.draw(screen)
        if time_stars == 100:
            time_stars = 0
            for _ in range(3):
                star = Point()
                point_sprites.add(star)
        point_sprites.draw(screen)
        point_sprites.update()
        NPS_sprites.update()
        bullets.update()
        eploude_sprite.draw(screen)
        eploude_sprite.update()
        hits = pygame.sprite.groupcollide(NPS_sprites, bullets, True, True)
        for hit in hits:
            expl = Explosion(hit.rect.center, 'lg')
            eploude_sprite.add(expl)
            nps = NPS()
            NPS_sprites.add(nps)
        clock.tick(fps)
        pygame.display.flip()
