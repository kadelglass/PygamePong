import pygame
BLACK = (0, 0, 0)

# The class is a paddle and derives from the Sprite class in pygame.

class Paddle(pygame.sprite.Sprite):


    # Constructor for the paddle
    def __init__(self, color, width, height):
        # Initialize the parent class (Sprite) constructor
        super().__init__()

        # --Sets the background of the paddle to transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400