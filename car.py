import os
import pygame


width, height = 300, 300


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


class Car(pygame.sprite.Sprite):
    image = load_image("car.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height

    def update(self, *args):
        pass