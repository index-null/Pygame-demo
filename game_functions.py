import pygame
import sys



def check_keydown_events(_ship, _event, _screen):
    if _event.type == pygame.KEYDOWN:
        if _event.key == pygame.K_LEFT:
            _ship.moving_left = True
        if _event.key == pygame.K_RIGHT:
            _ship.moving_right = True
        if _event.key == pygame.K_UP:
            _ship.moving_up = True
        if _event.key == pygame.K_DOWN:
            _ship.moving_down = True

        if _event.key == pygame.K_SPACE:
            _ship.is_shooting = True


def check_keyup_events(_ship, _event):
    if _event.type == pygame.KEYUP:
        if _event.key == pygame.K_LEFT:
            _ship.moving_left = False
        if _event.key == pygame.K_RIGHT:
            _ship.moving_right = False
        if _event.key == pygame.K_UP:
            _ship.moving_up = False
        if _event.key == pygame.K_DOWN:
            _ship.moving_down = False

        if _event.key == pygame.K_SPACE:
            _ship.is_shooting = False


def check_events(_ship, _screen, _bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        check_keydown_events(_ship=_ship, _event=event, _screen=_screen)

        check_keyup_events(_ship=_ship, _event=event)


def update_screen(_screen, _ship, _static_settings, _bullets, _background):
    _screen.blit(_background, (0, 0))

    _ship.update_status()

    _ship.blitme()

    for bullet in _bullets.sprites():
        bullet.update()
        bullet.blitme()

    pygame.display.flip()


def transform_scale_of_image(_image_path, _width, _height):
    _image = pygame.image.load(_image_path).convert()
    return pygame.transform.scale(_image, size=(_width, _height))
