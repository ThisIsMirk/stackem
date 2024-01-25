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
        self.image = pygame.Surface((50,20))
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.x = 5
        self.rect.y = 580
        self.speed = 5
        self.direction = 1

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.right >= WIDTH:
            self.direction = -1
        
        elif self.rect.left <= 0:
            self.direction = 1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mirk's Stack 'em")


clock = pygame.time.Clock()

white_block = Block()

# all_sprites = pygame.sprite.Group()
# blocks = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if random.random() < 0.02:
    #     new_block = Block()
    #     all_sprites.add(new_block)
    #     blocks.add(new_block)
            

    white_block.update()

    screen.fill((0,0,0))

    # for block in blocks:
    screen.blit(white_block.image, white_block.rect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()

