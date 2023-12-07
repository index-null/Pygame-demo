import pygame
from pygame.sprite import Sprite
from settings import DynamicSettings


class Bullet(Sprite):
    """A class to represent a bullet fired from the ship"""

    def __init__(self, _screen, _ship):
        """Initialize the bullet and set its starting position"""
        super().__init__()
        self.screen = _screen

        self.image = pygame.image.load("images/bullet.png")
        self.rect = self.image.get_rect()

        self.speed = DynamicSettings().bullet_speed

        self.rect.bottom = _ship.rect.top
        self.rect.centerx = _ship.rect.centerx

    def blitme(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the bullet up the screen"""
        self.rect.y -= self.speed

        if self.rect.bottom < 0:
            self.kill()
