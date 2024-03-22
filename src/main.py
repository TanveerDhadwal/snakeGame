import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

running = True
tokens = pygame.sprite.Group()
direction = -1
class Token(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def moveDown(self):
        self.rect.move_ip(0, 10)
    def moveUp(self):
        self.rect.move_ip(0, -10)
    def moveRight(self):
        self.rect.move_ip(10, 0)
    def moveLeft(self):
        self.rect.move_ip(-10, 0)
    def move(self):
        if direction == 1:
            self.moveUp()
        if direction == 2:
            self.moveDown()
        if direction == 3:
            self.moveRight()
        if direction == 4:
            self.moveLeft()

coin = Token(random.randrange(0, 1280), random.randrange(0, 720))
tokens.add(coin)
snake = Snake(random.randrange(0, 1280), random.randrange(0, 720))
tokens.add(snake)
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if keys[pygame.K_UP]:
            direction = 1
        if keys[pygame.K_DOWN]:
            direction = 2
        if keys[pygame.K_RIGHT]:
            direction = 3
        if keys[pygame.K_LEFT]:
            direction = 4
    snake.move()
    screen.fill((0, 0, 0))
    tokens.update()
    tokens.draw(screen)
    pygame.display.flip()
    clock.tick(10)



pygame.quit()