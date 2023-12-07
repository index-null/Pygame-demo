import pygame
import sys


def run_game():
    screen = pygame.display.set_mode((800, 1200))
    pygame.display.set_caption('Alien Invasion')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    run_game()