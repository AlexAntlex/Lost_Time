import pygame
import sqlite3
import sys

pygame.init()

number = 0
menu = True
option = False
rate = False

pygame.font.init()

bgcolor = (51, 51, 51)
font_color = (255, 255, 153)
highlite_color = (153, 102, 255)
font = pygame.font.SysFont('agencyfb', 65)
surface_width = 1200
surface_height = 700

surface_menu = pygame.display.set_mode([surface_width, surface_height])
pygame.display.set_caption("Lost Time")
surface_menu.fill(bgcolor)

fps = 10
clock = pygame.time.Clock()

mus_on = True
pygame.mixer.init()
snd = pygame.mixer.Sound('car.ogg')
music = ''


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


def main_menu():
    surface_menu.fill(bgcolor)
    DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80, (surface_height / 2) - 200)
    DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
    DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
    DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
    pygame.display.update()


def menu_option():
    surface_menu.fill(bgcolor)
    DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
             (surface_height / 2) - 200)
    DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
    DrawText('Rating', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
    DrawText('Back to menu', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
    pygame.display.update()


def running_menu():
    global number, option, menu
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        if number == 0:
            number += 1
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
        elif number == 1:
            number += 1
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        else:
            number = 0
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_UP]:
        if number == 0:
            number = 2
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        elif number == 1:
            number = 0
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
        else:
            number = 1
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_RETURN]:
        if number == 1:
            option = True
            menu = False
            surface_menu.fill(bgcolor)
            menu_option()
        elif number == 0:
            pass
        elif number == 2:
            pygame.quit()
            sys.exit()
        number = 0


def running_option():
    global number, option, music, menu, mus_on, rate
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        if number == 0:
            number += 1
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Rating', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Back to menu', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
        elif number == 1:
            number += 1
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Rating', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Back to menu', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        else:
            number = 0
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Rating', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Back to menu', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_UP]:
        if number == 0:
            number = 2
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Rating', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Back to menu', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        elif number == 1:
            number = 0
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Rating', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Back to menu', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
        else:
            number = 1
            surface_menu.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Rating', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Back to menu', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_RETURN]:
        if number == 1:
            rating()
            option = False
            rate = True
        elif number == 0:
            if mus_on:
                mus_on = False
            else:
                mus_on = True
            music = play_music()
            menu_option()
        elif number == 2:
            option = False
            menu = True
            main_menu()
        number = 0

    if key[pygame.K_ESCAPE]:
        option = False
        menu = True
        main_menu()
        number = 0


def rating():
    surface_menu.fill(bgcolor)
    pygame.display.update()
    DrawText('Rating', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
             (surface_height / 2) - 200)
    con = sqlite3.connect('rating.db')
    cur = con.cursor()
    result = cur.execute("""SELECT users, score FROM Score ORDER BY score DESC""").fetchmany(5)
    b = 110
    for elem in result:
        a = str(result.index(elem) + 1) + '. ' + elem[0] + ' - ' + str(elem[1]) + ' points'
        DrawText(a, font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - b)
        b -= 70
        con.commit()
    con.close()
    DrawText('Back to options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 270, True)


def running_rating():
    global rate, option
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE] or key[pygame.K_RETURN]:
        rate = False
        option = True
        menu_option()


pygame.mouse.set_visible(False)
music = play_music()
main_menu()

while True:
    if menu:
        running_menu()
    elif option:
        running_option()
    elif rate:
        running_rating()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(fps)