import pygame
import sys


def run_game():
    screen = pygame.display.set_mode((800, 1600))
    pygame.display.set_caption('Alien Invasion')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()



if __name__ == '__main__':
    pass