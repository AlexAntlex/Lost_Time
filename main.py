import pygame
from car import Car

pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)

running = True
clock = pygame.time.Clock()
fps = 30

all_sprites = pygame.sprite.Group()
car = Car()
all_sprites.add(car)

while running:
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        car.rect.y -= 10
    if key[pygame.K_DOWN]:
        car.rect.y += 10
    if key[pygame.K_LEFT]:
        car.rect.x -= 10
    if key[pygame.K_RIGHT]:
        car.rect.x += 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    clock.tick(fps)
    pygame.display.flip()
