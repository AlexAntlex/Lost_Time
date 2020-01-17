import pygame
import sqlite3
import sys

from game import game
from load_files import load_music

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
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
area = screen.get_rect()
surface_width = area[2]
surface_height = area[3]

pygame.display.set_caption("Lost Time")
screen.fill(bgcolor)

fps = 10
clock = pygame.time.Clock()

mus_on = True
pygame.mixer.init()
snd = load_music('start_menu.ogg')
music = ''


def play_music():
    if mus_on:
        music = 'Sound ON'
        snd.play(-1, 0, 0)
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
    screen.fill(bgcolor)
    DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80, (surface_height / 2) - 200)
    DrawText('Start', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
    DrawText('Options', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
    DrawText('Quit', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)
    pygame.display.update()


def menu_option():
    screen.fill(bgcolor)
    DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
             (surface_height / 2) - 200)
    DrawText(music, font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
    DrawText('Rating', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
    DrawText('Back to menu', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)
    pygame.display.update()


def running_menu():
    global number, option, menu
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]:
        if number == 0:
            number += 1
            screen.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Quit', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)
        elif number == 1:
            number += 1
            screen.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        else:
            number = 0
            screen.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Options', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_UP]:
        if number == 0:
            number = 2
            screen.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        elif number == 1:
            number = 0
            screen.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Options', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)
        else:
            number = 1
            screen.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Quit', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_RETURN]:
        if number == 1:
            option = True
            menu = False
            screen.fill(bgcolor)
            menu_option()
        elif number == 0:
            snd.stop()
            game()
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
            screen.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Rating', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Back to menu', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)
        elif number == 1:
            number += 1
            screen.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Rating', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Back to menu', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        else:
            number = 0
            screen.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Rating', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Back to menu', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)

    if key[pygame.K_UP]:
        if number == 0:
            number = 2
            screen.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Rating', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Back to menu', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
        elif number == 1:
            number = 0
            screen.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Rating', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Back to menu', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)
        else:
            number = 1
            screen.fill(bgcolor)
            DrawText('Options', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText(music, font, screen, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Rating', font, screen, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Back to menu', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 30)

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
    screen.fill(bgcolor)
    pygame.display.update()
    DrawText('Rating', (pygame.font.SysFont('agencyfb', 80)), screen, (surface_width / 2) - 80,
             (surface_height / 2) - 200)
    con = sqlite3.connect('rating.db')
    cur = con.cursor()
    result = cur.execute("""SELECT users, score FROM Score ORDER BY score DESC""").fetchmany(5)
    b = 110
    for elem in result:
        a = str(result.index(elem) + 1) + '. ' + elem[0] + ' - ' + str(elem[1]) + ' points'
        DrawText(a, font, screen, (surface_width / 2) - 65, (surface_height / 2) - b)
        b -= 70
        con.commit()
    con.close()
    DrawText('Back to options', font, screen, (surface_width / 2) - 65, (surface_height / 2) + 270, True)


def running_rating():
    global rate, option
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE] or key[pygame.K_RETURN]:
        rate = False
        option = True
        menu_option()


pygame.mouse.set_visible(False)
music = play_music()


def start_menu():
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