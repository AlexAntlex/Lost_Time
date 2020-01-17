import pygame
import sys
from load_files import load_image
from write_ur_name import fin

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
area = screen.get_rect()
WIDTH = area[2]
HEIGHT = area[3]

background = pygame.transform.scale(load_image('farback.png'), (WIDTH, HEIGHT))
background_rect = background.get_rect()
clock = pygame.time.Clock()
fps = 60


def terminate():
    pygame.quit()
    sys.exit()


bullets = pygame.sprite.Group()
gamer_sprite = pygame.sprite.Group()
NPS_sprites = pygame.sprite.Group()
point_sprites = pygame.sprite.Group()
icon_sprite = pygame.sprite.Group()


def pause(stop):
    font = pygame.font.SysFont('agencyfb', 80)
    font_2 = pygame.font.SysFont('agencyfb', 50)
    text = 'pause'
    text_3 = ' or Press ESC to return'
    text_2 = 'Press BACKSPACE to exit the game.'
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    stop = False
                if event.key == pygame.K_m:
                    pass
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
        pygame.display.update()
        clock.tick(15)


def game_over(score):
    font = pygame.font.SysFont('agencyfb', 50)
    font_2 = pygame.font.SysFont('agencyfb', 80)
    text_1 = 'Game Over'
    text_2 = f'Your Score: {score}'
    text_3 = 'Press BACKSPACE to exit the game.'
    fin(score)
    while True:
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or key[pygame.K_BACKSPACE]:
                terminate()
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
        pygame.display.update()
        clock.tick(15)


explosion_anim = {}
explosion_anim['lg'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = load_image(filename)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)


def draw_text(surf, text, x, y):
    font = pygame.font.SysFont('agencyfb', 50)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)