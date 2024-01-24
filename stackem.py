import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
FPS = 30
WHITE = (255,255,255)

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mirk's Stack 'em")

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.random() < 0.02:
        new_block = Block()
        all_sprites.add(new_block)
        blocks.add(new_block)

    all_sprites.update()

    screen.fill((0,0,0))

    for block in blocks:
        screen.blit(block.image, block.rect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()