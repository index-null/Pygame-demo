import pygame
import time
from bullet import Bullet
from settings import DynamicSettings


class Ship:
    def __init__(self, _screen, _speed, _bullets):
        self.screen = _screen
        self.image = pygame.image.load("images/plane.png")

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.lives = DynamicSettings().lives

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.is_shooting = False

        self.speed = _speed
        self.bullets = _bullets
        self.last_shot_time = 0
        self.shooting_speed = DynamicSettings().shooting_speed
        self.shooting_delay = DynamicSettings().delay
        self.shooting_sound = pygame.mixer.Sound('sounds/interactive_sounds/shoot.mp3')

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def boom(self):
        boom_sound = pygame.mixer.Sound('sounds/interactive_sounds/boom.mp3')
        boom_sound.play()
        pygame.time.wait(1000)

    def update_status(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.speed

        if self.is_shooting:
            current_time = time.time()
            last_time = self.last_shot_time
            if current_time - last_time > self.shooting_delay:
                self.shooting_sound.play()
                self.bullets.add(Bullet(self.screen, self))
                self.last_shot_time = current_time
