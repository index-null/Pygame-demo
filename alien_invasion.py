import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import StaticSettings, DynamicSettings
from ship import Ship


def run_game():
    pygame.init()
    static_settings = StaticSettings()
    dynamic_settings = DynamicSettings()

    screen = pygame.display.set_mode((static_settings.screen_width, static_settings.screen_height))
    pygame.display.set_caption(static_settings.caption)
    bullets = Group()
    ship = Ship(
        _screen=screen,
        _speed=dynamic_settings.ship_speed,
        _bullets=bullets
    )

    background = gf.transform_scale_of_image(
        _image_path=static_settings.background1,
        _width=static_settings.screen_width,
        _height=static_settings.screen_height
    )

    while True:
        gf.check_events(_ship=ship, _screen=screen, _bullets=bullets)

        gf.update_screen(_screen=screen, _static_settings=static_settings, _ship=ship, _bullets=bullets, _background=background)


if __name__ == '__main__':
    run_game()
