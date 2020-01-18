import pygame
import sys

pygame.init()

bgcolor = (51, 51, 51)
font_color = (255, 255, 153)
highlite_color = (153, 102, 255)
font = pygame.font.SysFont('agencyfb', 65)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
area = screen.get_rect()
surface_width = area[2]
surface_height = area[3]

surface_menu = pygame.display.set_mode([surface_width, surface_height])
pygame.display.set_caption("Lost Time")
surface_menu.fill(bgcolor)

fps = 10
clock = pygame.time.Clock()

mus_on = True
pygame.mixer.init()
snd = pygame.mixer.Sound('car.ogg')
music = ''

numb = 0


def play_music():
    if mus_on:
        music = 'Sound ON'
        snd.play(-1,0,0)
    else:
        music = 'Sound OFF'
        snd.stop()
    return music


def DrawText(text, font, surface_menu, x, y, selected=False):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    if selected:
        highlight = pygame.Surface((len(text) * 33, 65))
        highlight.fill(highlite_color)
        surface_menu.blit(highlight, [x - 15, y])
    surface_menu.blit(textobj, textrect)


def new_option():
    surface_menu.fill(bgcolor)
    DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
             (surface_height / 2) - 200)
    DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
    DrawText('Back to pause', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
    DrawText('Exit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
    pygame.display.update()


def running_new():
    global numb, music, mus_on

    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        if numb == 0:
            numb += 1
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Back to pause', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Exit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
        elif numb == 1:
            numb += 1
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Back to pause', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Exit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        else:
            numb = 0
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Back to pause', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Exit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_UP]:
        if numb == 0:
            numb = 2
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Back to pause', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Exit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        elif numb == 1:
            numb = 0
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Back to pause', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Exit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
        else:
            numb = 1
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Back to pause', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Exit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_RETURN]:
        if numb == 1:
            pass
        elif numb == 0:
            if mus_on:
                mus_on = False
            else:
                mus_on = True
            music = play_music()
            new_option()
        elif numb == 2:
            pygame.quit()
            sys.exit()
        numb = 0

    if key[pygame.K_ESCAPE]:
        pass


pygame.mouse.set_visible(False)
music = play_music()
new_option()

while True:
    running_new()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(fps)