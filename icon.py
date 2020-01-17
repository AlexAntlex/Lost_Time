import pygame
from had_files import load_image, WIDTH, HEIGHT


class GameIcon(pygame.sprite.Sprite):
    icons = [load_image('Sun_00000.png'),
             load_image('Sun_00001.png'),
             load_image('Sun_00002.png'),
             load_image('Sun_00003.png'),
             load_image('Sun_00004.png'),
             load_image('Sun_00005.png'),
             load_image('Sun_00006.png'),
             load_image('Sun_00007.png'),
             load_image('Sun_00008.png'),
             load_image('Sun_00009.png'),
             load_image('Sun_00010.png'),
             load_image('Sun_00011.png'),
             load_image('Sun_00012.png'),
             load_image('Sun_00013.png'),
             load_image('Sun_00014.png')]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = GameIcon.icons[0]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2.5
        self.rect.y = HEIGHT / 2.2 - 60
        self.count = 0

    def update(self):
        self.count += 1
        if self.count > 14:
            self.count = 0
        self.image = GameIcon.icons[self.count]