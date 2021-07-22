import pygame
from random import randint
BLACK = (0, 0, 0)

class Ball(pygame.sprite.Sprite):

    # Constructor for the ball
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #pygame.draw.circle(self.image, color, [0, 0, width, height])
        pygame.draw.circle(self.image, color, (width/2, height/2), height/2)
        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)






