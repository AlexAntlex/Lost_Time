import pygame
import sys

number = 0
pygame.font.init()

bgcolor = (51, 51, 51)
font_color = (255, 255, 153)
highlite_color = (153, 102, 255)
font = pygame.font.SysFont('agencyfb', 65)
surface_width = 800
surface_height = 600

surface_menu = pygame.display.set_mode([surface_width, surface_height])
pygame.display.set_caption("Lost Time")
surface_menu.fill(bgcolor)

fps = 10
clock = pygame.time.Clock()

def DrawText(text, font, surface_menu, x, y, selected=False):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    if selected:
        highlight = pygame.Surface((len(text) * 33, 65))
        highlight.fill(highlite_color)
        surface_menu.blit(highlight, [x - 15, y])
    surface_menu.blit(textobj, textrect)


DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80, (surface_height / 2) - 200)
DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
pygame.display.update()

pygame.init()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
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
            pygame.display.update()
        elif number == 1:
            number += 1
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                    (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
            pygame.display.update()
        else:
            number = 0
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
            pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        if number == 0:
            number = 2
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                    (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30, True)
            pygame.display.update()
        elif number == 1:
            number = 0
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                    (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110, True)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
            pygame.display.update()
        else:
            number = 1
            surface_menu.fill(bgcolor)
            DrawText('Lost Time', (pygame.font.SysFont('agencyfb', 80)), surface_menu, (surface_width / 2) - 80,
                     (surface_height / 2) - 200)
            DrawText('Start', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 110)
            DrawText('Options', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) - 40, True)
            DrawText('Quit', font, surface_menu, (surface_width / 2) - 65, (surface_height / 2) + 30)
            pygame.display.update()
    clock.tick(fps)
    pygame.display.flip()




