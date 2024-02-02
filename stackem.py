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
        self.speed = 40
        self.direction = 1
        self.move_counter = 0
        self.stopped = False

    def update(self):
        if not self.stopped:
            self.move_counter += abs(self.speed * self.direction)

            if self.move_counter >= 200:  # Adjust this threshold as needed
                self.rect.x += self.speed * self.direction
                self.move_counter = 0  # Reset the move counter

            if self.rect.right >= WIDTH:
                self.direction = -1
            
            elif self.rect.left <= 0:
                self.direction = 1
    
    def stop(self):
        self.stopped = True

    def start(self):
        self.stopped = False


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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                white_block.stop()


    white_block.update()

    screen.fill((0,0,0))

    screen.blit(white_block.image, white_block.rect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()

