import pygame
import sys
import sqlite3
from load_files import load_music

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

clock = pygame.time.Clock()
input_box = pygame.Rect((surface_width / 2) - 70, (surface_height / 2) - 100, 200, 200)
color_active = pygame.Color(153, 102, 255)
text = ''
done = False


def DrawText(text, font, surface_menu, x, y, selected=False):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    if selected:
        highlight = pygame.Surface((len(text) * 33, 65))
        highlight.fill(highlite_color)
        surface_menu.blit(highlight, [x - 15, y])
    surface_menu.blit(textobj, textrect)


def ur_name():
    surface_menu.fill(bgcolor)
    DrawText('Put your name:', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
             (surface_height / 2) - 200)


def running_add(score):
    global done, text
    con = sqlite3.connect('rating.db')
    cur = con.cursor()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cur.execute("INSERT INTO Score(users, score) VALUES ('%s', '%d')" % (text, score))
                    con.commit()
                    con.close()
                    text = ''
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        ur_name()
        txt_surface = font.render(text, True, font_color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x, input_box.y + 5))
        pygame.draw.rect(screen, bgcolor, input_box, 2)
        pygame.display.flip()


pygame.mouse.set_visible(False)


def fin(score):
    ur_name()
    while True:
        running_add(score)
        if done:
            return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        clock.tick(30)
