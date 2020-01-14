import os
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
