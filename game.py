import pygame
from gamer import Gamer
from enemies import NPS, Explosion
from good_points import Point
from had_files import screen, WIDTH, HEIGHT, background, background_rect, clock, fps, \
    terminate, gamer_sprite, NPS_sprites, bullets, point_sprites, icon_sprite, pause, explosion_anim, draw_text

from icon import GameIcon
from load_files import load_music

pygame.init()
pygame.mouse.set_visible(False)
pygame.time.set_timer(pygame.USEREVENT, 1000)

gamer = Gamer()
gamer_sprite.add(gamer)

for _ in range(7):
    nps = NPS()
    NPS_sprites.add(nps)

for _ in range(3):
    star = Point()
    point_sprites.add(star)

icon = GameIcon()
icon_sprite.add(icon)

eploude_sprite = pygame.sprite.Group()
score = 0


def game():
    """Основной игровой цикл"""
    global score, nps
    counter, text = 4, '3'.rjust(3)
    snd = load_music('game.ogg')
    snd.play()
    while True:
        font = pygame.font.SysFont('agencyfb', 62)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        stop = True
                        pause(stop)
                if event.key == pygame.K_SPACE:
                    gamer.shoot()
             # Счетчик в начале игры
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
            # После окончания отсчета начинается основной геймплей
            gamer_sprite.update()
            screen.fill((0, 0, 0))
            screen.blit(background, background_rect)
            bullets.draw(screen)
            gamer_sprite.draw(screen)
            NPS_sprites.draw(screen)
            point_sprites.draw(screen)
            point_sprites.update(gamer)
            NPS_sprites.update(gamer, score)
            bullets.update(nps)
            eploude_sprite.draw(screen)
            eploude_sprite.update()
            hits = pygame.sprite.groupcollide(NPS_sprites, bullets, True, True)
            # Реакция на столкновения врагов и выстрелов
            for hit in hits:
                score += 50 - hit.radius
                expl = Explosion(hit.rect.center, 'lg', explosion_anim)
                eploude_sprite.add(expl)
                nps = NPS()
                NPS_sprites.add(nps)
            # Реакция на столкновение игрока и звезд
            hits_2 = pygame.sprite.spritecollide(gamer, point_sprites, True)
            for _ in hits_2:
                score += 75
                star = Point()
                point_sprites.add(star)
            draw_text(screen, str(score),  WIDTH / 2, 10)
            clock.tick(fps)
            pygame.display.flip()
