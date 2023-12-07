import pygame
from random import randint
from pygame.sprite import Sprite
from settings import DynamicSettings


class Enemy(Sprite):
    def __init__(self, _screen):
        super().__init__()
        self.screen = _screen
        self.image = pygame.image.load("images/enemy.png")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.speed = DynamicSettings().enemy_speed
        self.rect.x = randint(0, int(self.screen_rect.right) - int(self.rect.width))
        self.rect.bottom = self.screen_rect.top

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.screen_rect.bottom:
            self.kill()
