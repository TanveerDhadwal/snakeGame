import pygame


pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Snake Game")

running = True
tokens = pygame.sprite.Group()

class Token(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



def makeSprite(name, x, y):
    name = Token(x, y)
    tokens.add(name)

makeSprite("coin",20,20)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    tokens.update()
    tokens.draw(screen)
    pygame.display.flip()



pygame.quit()