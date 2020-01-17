import pygame
from main_menu import start_menu


pygame.init()
pygame.mouse.set_visible(False)
pygame.time.set_timer(pygame.USEREVENT, 1000)

start_menu()