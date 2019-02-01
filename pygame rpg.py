import pygame
WIDTH = 400
HEIGHT = 300
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
Blue = (0, 255, 0)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("basic rpg")
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.centerx = x
        self.rect.centery = y
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -2

        elif keystate[pygame.K_RIGHT]:
            self.speedx = 2

        elif keystate[pygame.K_UP]:
            self.speedy = -2

        elif keystate[pygame.K_DOWN]:
            self.speedy = 2

        else:
            self.speedx = 0
            self.speedy = 0
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = HEIGHT


all_sprites = pygame.sprite.Group()
for i in range(1, 10):
    andy = Player(10*i , 100, Blue)
    all_sprites.add(andy)
player = Player(50, 100, RED)

all_sprites.add(player)



running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    screen.fill(WHITE)
pygame.quit()
