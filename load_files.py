import os
import pygame


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


def load_music(name):
    fullname = os.path.join('music', name)
    sound = pygame.mixer.Sound(fullname)
    return sound